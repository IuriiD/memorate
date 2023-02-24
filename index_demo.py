# This repo has both OpenAI responses hardcoded, may be used for demo or in case OpenAI API is down

import openai
import streamlit as st
from annotated_text import annotated_text
import time
import json
import random

import mysecrets

### State example
# TODO: A. Move options selection/enablement state into questions key. B. Remove nested questions.questions
# {
#   "render_questions_btn": false,
#   "questions": {
#     "questions": [
#       {
#         "question": "What is prompt engineering?",
#         "options": [
#           "The art of writing good intentional prompts that produce an output from a generative AI model",
#           "A more abstract version of programming",
#           "A super abstract programming of an AI model",
#           "A way to modify the mode or type of task that has been formed"
#         ],
#         "reference": "",
#         "correct_option_index": 0,
#         "was_answered": false,
#         "was_skipped": false
#       },
#       {
#         "question": "What is the best way to think about prompt engineering?",
#         "options": [
#           "As a way to modify the mode or type of task that has been formed",
#           "As a more abstract version of programming",
#           "As a super abstract programming of an AI model",
#           "As the next step in programming languages"
#         ],
#         "reference": "",
#         "correct_option_index": 1,
#         "was_answered": false,
#         "was_skipped": false
#       }
#     ],
#     "questionnaire_state": {
#       "questions_asked": 0,
#       "questions_skipped": 0
#     }
#   },
#   "options_state": {
#     "q1": {
#       "1": {
#         "selected": false,
#         "disabled": true
#       },
#       "2": {
#         "selected": true,
#         "disabled": true
#       },
#       "3": {
#         "selected": false,
#         "disabled": true
#       },
#       "4": {
#         "selected": false,
#         "disabled": true
#       },
#       "skip_q1": {
#         "selected": false,
#         "disabled": true
#       }
#     },
#     "q2": {
#       "1": {
#         "selected": true,
#         "disabled": true
#       },
#       "2": {
#         "selected": false,
#         "disabled": true
#       },
#       "3": {
#         "selected": false,
#         "disabled": true
#       },
#       "4": {
#         "selected": false,
#         "disabled": true
#       },
#       "skip_q2": {
#         "selected": false,
#         "disabled": true
#       }
#     }
#   },
#   "generate_q_btn": {
#     "disabled": true
#   },
#   "user_score": 0,
#   "questions_rendered": true
# }

openai.organization = mysecrets.OPENAI_ORG
openai.api_key = mysecrets.OPENAI_KEY

### Constants
PROJECT_NAME = 'Memorate' # temp
PROJECT_IDEA = 'Improve memorization by answering questions'
TEXT_AREA_INSTRUCTION = 'Paste some text and get asked about it. Max 1300 characters'
DUMMY_TEXT = 'Ukraine has been removed from the list of countries where the artificial intelligence chatbot ChatGPT is blocked. Ukrainian Deputy Prime Minister - Minister of Digital Transformation Mykhailo Fedorov announced this on Telegram, Ukrinform reports. "ChatGPT is now available in Ukraine. The team of the Ministry of Digital Transformation worked for a long time on this decision - official letters, calls and a meeting with the management. Finally, we managed to correct the injustice. Ukraine was removed from the list of countries where ChatGPT is blocked," he wrote. The program will not work only in the territories temporarily occupied by Russia. ChatGPT is an artificial intelligence chatbot developed by AI startup OpenAI and capable of working in dialog mode, which supports requests in different languages.'
MAX_INPUT_LEN_CHARS = 1300
SEPARATOR = '<highlight>'
CORRECT_MARK = '^'

### Functions
def get_openai_completion(prompt):
    print('\n\nOPENAI-PROMPT:', prompt)
    try:
        res = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=400, temperature=0.1)
        print('\n\nOPENAI-RESPONSE:', res)
        return res.choices[0]['text'] or None
    except e as e:
        st.write(e)

def openai_get_proofs(answer_options, input_text):
    options_prompt = []
    for idx, option in enumerate(answer_options, start=1):
        options_prompt.append(f'{idx}. {option}\n')
    prompt = f"""In the following text find the sentences which correspond to the following phrases:\n{''.join(options_prompt)}\n{input_text.rstrip('.')}
    """
    return "\n1. ChatGPT is an artificial intelligence chatbot developed by AI startup OpenAI and capable of working in dialog mode, which supports requests in different languages\n2. Ukrainian Deputy Prime Minister - Minister of Digital Transformation Mykhailo Fedorov announced this on Telegram, Ukrinform reports. \"ChatGPT is now available in Ukraine. The team of the Ministry of Digital Transformation worked for a long time on this decision - official letters, calls and a meeting with the management.\n3. Finally, we managed to correct the injustice. Ukraine was removed from the list of countries where ChatGPT is blocked,\" he wrote."
    return get_openai_completion(prompt)

def openai_get_questions(input_text, questions_number=3):
    prompt = f'''Ask {questions_number} multi-choice questions to the following text and mark the correct answer with "{SEPARATOR}":\n\n{input_text}'''
    return "\n\nQ1: What is ChatGPT?\nA. An artificial intelligence chatbot ^\nB. A program developed by AI startup OpenAI\nC. A chatbot capable of working in dialog mode\n\nQ2: What did the Ukrainian Deputy Prime Minister - Minister of Digital Transformation do to make ChatGPT available in Ukraine?\nA. He wrote an official letter ^\nB. He held a meeting with the management\nC. He made a call\n\nQ3: Where will ChatGPT not work?\nA. In Ukraine ^\nB. In the territories temporarily occupied by Russia\nC. In different languages"
    return get_openai_completion(prompt)

# removes the leading "Q1: " for questions,
# or "A. " for response options,
# or "1. " for proofs; might not be 100% reliable
def remove_string_identifier(raw_q):
    parts = raw_q.split(' ')
    without_q_number = parts[1:]
    return ' '.join(without_q_number)

# in some queries to OpenAI all multi-choice questions
# generated had correct answer as the 1st option - not good
def shuffle_options(options, old_correct_idx):
    correct_option = options[old_correct_idx]
    randomised_options = random.sample(options, len(options))
    new_correct_idx = randomised_options.index(correct_option)
    return randomised_options, new_correct_idx

# Expects a string like
# "\n\nQ1: The 1st question?\nA. Option A, marked as correct with^\nB. The 2nd answer\nC. There may be 3-4 options\n\nQ2: Question #2\nA. ...."
# Returns an array of question objects (with keys questions, options, reference, correct_option_index, was_answered, was_skipped)
def openai_res_to_questions(openai_resp_questions):
    res = []
    leading_trailing_new_lines_removed = openai_resp_questions.strip('\n')
    paragraphs = leading_trailing_new_lines_removed.split('\n\n')
    
    for paragraph in paragraphs:
        if not paragraph: continue
        parts = paragraph.split('\n')
        the_question = remove_string_identifier(parts[0]) # remove leading "Q1: " or "1. "
        options_with_numbers = parts[1:]
        options = [remove_string_identifier(option) for option in options_with_numbers] # remove eg "A. "
        options_randomised = random.sample(options, len(options)) # sometimes all the questions may have correct answer at idx 0
        q = {}
        for idx, el in enumerate(options_randomised):
            if CORRECT_MARK in el:
                q['correct_option_index'] = idx
                options_randomised[idx] = el.replace(CORRECT_MARK, '').rstrip()
        q['question'] = the_question
        q['options'] = options_randomised
        q['was_answered'] = False
        q['was_skipped'] = False
        res.append(q)
    return res

# Expects a string like
# "\n\n1. \"Some response, in double quotes or without them\"\n2. \"The 2nd proof\"
# The number of proofs should correspond to the number of questions
# Proofs may not 100% coincide with the original text. My observation: usually the ending
# of the returned proof coincides Ok, while the beginning may be rephrased
# Returns a list of (segments of the original text with the proofs + some overlapping text)
# May consider also using non-OpenAI approaches like
# https://stackoverflow.com/questions/17740833/checking-fuzzy-approximate-substring-existing-in-a-longer-string-in-python
def openai_res_to_references(openai_resp_proofs, input_text):
    OVERLAP_CHARS = 50 # how many caracters before and after the segment should be taken
    paragraphs = openai_resp_proofs.replace('\n\n', '').strip('\n').split('\n')
    proofs = []
    for paragraph in paragraphs:
        if not paragraph: continue
        without_number = remove_string_identifier(paragraph)
        highlighted_substr = without_number.strip('"').strip("'").strip('.')
        substr_idx_start = -1
        input_text_lower = input_text.lower()
        highlighted_substr_lower = highlighted_substr.lower()
        highlighted_words = highlighted_substr_lower.split(' ')
        
        while len(highlighted_words):
            substr_idx_start = input_text_lower.find(' '.join(highlighted_words))
            if substr_idx_start >= 0:
                break
            highlighted_words = highlighted_words[1:] # remove the leading word of the searched substr (lowercased)
            highlighted_substr = ' '.join(highlighted_substr.split(' ')[1:]) # and from the original substr (not lowercased)
        if substr_idx_start < 0:
             proofs.append(input_text)
        else:
            leading_overlap_start_idx = substr_idx_start - OVERLAP_CHARS if substr_idx_start - OVERLAP_CHARS >= 0 else 0
            leading_overlap = input_text[leading_overlap_start_idx:substr_idx_start]
            trailing_overlap_start_idx = substr_idx_start + len(highlighted_substr)
            trailing_overlap = input_text[trailing_overlap_start_idx:trailing_overlap_start_idx+OVERLAP_CHARS]
            proofs.append(f'{leading_overlap}{SEPARATOR}{highlighted_substr}{SEPARATOR}{trailing_overlap}')
    return proofs

# Gets the list of objects with questions and answer options,
# returns a list of correct options (to be used for fetching proofs)
def extract_correct_answers(questions):
    res = []
    for question in questions:
        correct_option_idx = question['correct_option_index'] # starts from 0
        correct_option = question['options'][correct_option_idx]
        res.append(correct_option)
    return res

# adds the proofs to each question as question[n]['correct_option_index']
# assumes that the number of proofs and their order corresponds to the questions
def add_proofs(proofs, questions):
    for idx, proof in enumerate(proofs):
        questions[idx]['reference'] = proof
    return questions

# Gets the text pasted by the user, does pre-processing (if needed), 
# generates questions using OpenAI API
def get_questions(user_input):
    # temp load a ready json
    # with open('data.json') as f:
    #     data = json.load(f)
    # return data
    openai_questions = openai_get_questions(user_input)
    questions = openai_res_to_questions(openai_questions)
    # print('\nquestions\n', questions)
    correct_options = extract_correct_answers(questions)
    # print('\n\ncorrect_options\n', correct_options)
    openai_proofs = openai_get_proofs(correct_options, user_input)
    proofs = openai_res_to_references(openai_proofs, user_input)
    # print('\n\nproofs\n', proofs)
    questions_with_proofs = add_proofs(proofs, questions)
    print('\n\nready_questions=', questions_with_proofs)
    return { 'questions': questions_with_proofs }

def generate_response_options_states(questions):
    response_options_state = {}
    for idx, question in enumerate(questions, start=1):
        question_index = f'q{idx}'
        response_options_state[question_index] = {}
        for op_idx, _ in enumerate(question['options'], start=1):
            response_options_state[question_index][str(op_idx)] = { 'selected': 0, 'disabled': 0 }
        skip_key = f'skip_{question_index}'
        response_options_state[question_index][skip_key] = { 'selected': 0, 'disabled': 0 }
    return response_options_state

def initialize_state(user_input):
    st.session_state.questions_rendered = False
    st.session_state['generate_q_btn'] = { 'disabled': False }
    st.session_state.user_score = 0
    questions = get_questions(user_input)
    st.session_state.questions = questions
    st.session_state.options_state = generate_response_options_states(questions['questions'])
    st.session_state.questionnaire_state = { 'questions_asked': [], 'questions_skipped': [], 'correct': [] }

def generate_q_btn_disabled(state):
        # initialize_state('temp')
        st.session_state.generate_q_btn['disabled'] = state


### Render UI and combine all together
st.title(PROJECT_NAME)
st.write(PROJECT_IDEA)

tab_text, tab_youtube = st.tabs(['Text', 'Youtube'])

with tab_text:
    user_input = st.text_area(TEXT_AREA_INSTRUCTION, 
                 DUMMY_TEXT,
                 on_change=generate_q_btn_disabled, args=(False,),
                 max_chars=MAX_INPUT_LEN_CHARS)
    
    if 'questions_rendered' not in st.session_state:
        initialize_state(user_input)
    
    # Debug
    st.write(st.session_state)
    
    st.button(
        'Generate questions', 
        key='render_questions_btn', 
        on_click=generate_q_btn_disabled, args=(True,), # set button as disabled in state
        disabled=st.session_state.generate_q_btn['disabled'] # update disablement according to the state
        )

    # render the following only if "Generate questions" button was clicked 
    # or questions_rendered flag was set True
    if st.session_state.render_questions_btn or st.session_state.questions_rendered:
        
        # >> Showing the loader (only once after "Generate Q" button click)
        # https://docs.streamlit.io/library/api-reference/layout/st.empty
        processing_done_str = "Processing..... Done"
        with st.empty():
            if st.session_state.questions_rendered:
                st.write(processing_done_str)
            else:
                for seconds in range(2): # this should be dynamic
                    st.write(f"Processing{'.' * seconds}")
                    time.sleep(1)
                st.write(processing_done_str)
        st.session_state.questions_rendered = True

        st.header('Questions:')

        def renderQuestions():
            def disable_options(question_options_state_keys):
                for question_option in question_options_state_keys:
                    question_options_state_keys[question_option]['disabled'] = True
                
            # q_idx - the number part of the key in session_state['options_state'], eg. 1 (to be transformed into 'q1')
            # option_key_to_select - the name of the option key, which needs to be marked as key.selected = true, eg '1' or 'skip_q2'
            def mark_selected(q_idx, option_key_to_select):
                q_index_key = f'q{q_idx+1}'
                for option in st.session_state['options_state'][q_index_key]:
                    if option == option_key_to_select:
                        st.session_state['options_state'][q_index_key][option]['selected'] = True
                    else:
                        st.session_state['options_state'][q_index_key][option]['selected'] = False
                
            # q_idx = 0, index in session_state['questions']['questions']
            # q_state_key = {'1': {'selected': 0, 'disabled': 0}, '2': {'selected': 0, 'disabled': 0}, ...}
            # opt_idx_to_select: number = 2
            def mark_selected_disable_all_options(q_idx, q_state_key, option_key_to_select):
                mark_selected(q_idx, option_key_to_select)
                disable_options(q_state_key)

            def highlight_proof(reference):
                # reference is expected to contain only 1 substring, surrounded with separator
                COLOR = '#fea'
                parts = reference.split(SEPARATOR)
                hightlight_tuple = (parts[1], '', COLOR)
                return [
                    f'...{parts[0]}', hightlight_tuple, f'{parts[2]}...']
                
            # q_idx - question index (start=1), e.g. 1 for the 1st question (with index 0)
            # answer_status - enum('skipped', 'correct', 'wrong')
            #  st.session_state.questionnaire_state = { 'questions_asked': [], 'questions_skipped': [], 'correct': [] }
            def update_score(q_idx, answer_status='wrong'):
                if q_idx not in st.session_state['questionnaire_state']['questions_asked']:
                    st.session_state['questionnaire_state']['questions_asked'].append(q_idx)
                    if answer_status == 'skipped':
                        st.session_state['questionnaire_state']['questions_skipped'].append(q_idx)
                    elif answer_status == 'correct':
                        st.session_state['questionnaire_state']['correct'].append(q_idx)
            
            def show_stats():
                print(st.session_state['questionnaire_state'])
                questions_asked = len(st.session_state['questionnaire_state']['questions_asked'])
                questions_skipped = len(st.session_state['questionnaire_state']['questions_skipped'])
                answered_correctly = len(st.session_state['questionnaire_state']['correct'])
                divide_by = questions_asked - questions_skipped or 1
                correct_prcnt = answered_correctly / divide_by * 100
                st.markdown(f':grey[Asked: {questions_asked} | skipped: {questions_skipped} | correct: {answered_correctly} ({correct_prcnt}%)]')
            
            def generate_q_options(q_idx, question_with_options, q_idx_started_1):
                options = {}
                q_idx_str = str(q_idx_started_1)
                
                # Generate options for UI and 
                # "handlers" to disable all options on click and select only the clicked option
                for idx, option in enumerate(question_with_options['options'], start=1):
                    idx_str = str(idx)
                    q_key = f'q{q_idx_str}'
                    options[idx_str] = st.checkbox(
                        option, 
                        value = st.session_state.options_state[q_key][idx_str]['selected'], 
                        on_change = mark_selected_disable_all_options, args=(q_idx, st.session_state['options_state'][q_key], idx_str,),
                        disabled = st.session_state.options_state[q_key][idx_str]['disabled']
                        )
                skip_option_key = f'skip_{q_key}'
                options[skip_option_key] = st.checkbox(
                    f'Mark question #{q_idx_started_1} as invalid and skip it', 
                    value = st.session_state.options_state[q_key][skip_option_key]['selected'], 
                    on_change = mark_selected_disable_all_options, args=(q_idx, st.session_state['options_state'][q_key], skip_option_key,),  
                    disabled = st.session_state.options_state[q_key][skip_option_key]['disabled']
                    ) 
                
                # Logic to check if the option selected is correct, react and update score
                correct_option_idx_key = str(st.session_state['questions']['questions'][q_idx]['correct_option_index']+1)
                
                for key in options:
                    value = options[key]
                    response_status = 'wrong'
                    if value:
                        if key == skip_option_key:
                            response_status = 'skipped'
                            st.write(f'☠ Ok, the question #{q_idx+1} was skipped and will be ignored')
                        elif key == correct_option_idx_key:
                            response_status = 'correct'
                            st.write('👍 Correct!')
                            annotated_text(*highlight_proof(st.session_state['questions']['questions'][q_idx]['reference']))
                        else:
                            response_status = 'wrong'
                            correct_option_idx = st.session_state['questions']['questions'][q_idx]['correct_option_index']
                            correct_option = st.session_state['questions']['questions'][q_idx]['options'][correct_option_idx]
                            st.markdown(f"😬 Unfortunately, no, the correct answer is *'{correct_option}'*")
                            annotated_text(*highlight_proof(st.session_state['questions']['questions'][q_idx]['reference']))
                        update_score(q_idx+1, response_status)
                        show_stats()

            
            def render_question_title(q_idx):
                st.text("")
                st.subheader(f'''Q{q_idx+1}. {st.session_state['questions']['questions'][q_idx]['question']}''')
            
            for idx, _ in enumerate(st.session_state['questions']['questions']):
                render_question_title(idx)
                generate_q_options(idx, st.session_state['questions']['questions'][idx], idx+1)
        
        renderQuestions()

with tab_youtube:
    url = st.text_input('Youtube video URL')