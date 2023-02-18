import streamlit as st
from annotated_text import annotated_text
import time
import json

### State example
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

### Constants
PROJECT_NAME = 'Memorate' # temp
PROJECT_IDEA = 'Improve memorization by answering questions'
TEXT_AREA_INSTRUCTION = 'Paste some text and get an interactive questionnaire generated for it'
DUMMY_TEXT = "prompt engineering is a emerging discipline within the world of generative Ai and it describes the art of writing good intentional prompts that produce an output from a generative AI model that we actually want and to a degree it is an R it's it's very hard to explain how to create a good product but to a larger extent there's a very logical process and way that we can go into creating problems that can be described and easily applied to produce better output from large language models and of course the generative art tools as well good prompts are the key to producing good outputs for these models using different types of prompts we can modify the mode or type of task that has been formed and we can even use prompts to train models to some degree and the performance of doing that is actually surprisingly good now there's a few things to learn with prompt engineering and I think one of the best ways to maybe think about this discipline is to think of it as a more abstract version of programming so throughout the last decades we've seen programming languages become more and more abstract prompts for AI models is almost like the next step it's a super abstract programming of an AI model and that's exactly how I want to approach this here I want to discuss prompts and building good prompts of AI models"

### Functions
# Gets the text pasted by the user, does pre-processing, 
# generates questions using OpenAI API
def get_questions(user_input):
    # temp load a ready json
    with open('data.json') as f:
        data = json.load(f)
    return data

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
        initialize_state('temp')
        st.session_state.generate_q_btn['disabled'] = state


### Render UI and combine all together
st.title(PROJECT_NAME)
st.write(PROJECT_IDEA)

tab_text, tab_youtube = st.tabs(['Text', 'Youtube'])

with tab_text:
    user_input = st.text_area(TEXT_AREA_INSTRUCTION, 
                 DUMMY_TEXT,
                 on_change=generate_q_btn_disabled, args=(False,))
    
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
                separator = '<highlight>'
                parts = reference.split(separator)
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