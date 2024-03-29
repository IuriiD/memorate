captions = [
  { "text": "today we're going to talk about", "start": 0.0, "duration": 4.68 },
  {
    "text": "abstractive or generative question and",
    "start": 1.76,
    "duration": 5.619
  },
  {
    "text": "answering and we're going to focus on",
    "start": 4.68,
    "duration": 4.74
  },
  {
    "text": "actually building or implementing",
    "start": 7.379,
    "duration": 4.26
  },
  {
    "text": "something like this using a few",
    "start": 9.42,
    "duration": 4.86
  },
  {
    "text": "different components but in the end what",
    "start": 11.639,
    "duration": 4.141
  },
  {
    "text": "we're going to essentially be able to",
    "start": 14.28,
    "duration": 4.86
  },
  {
    "text": "get is we're going to be able to ask a",
    "start": 15.78,
    "duration": 5.88
  },
  {
    "text": "question in natural language and we're",
    "start": 19.14,
    "duration": 5.82
  },
  {
    "text": "going to be able to return documents or",
    "start": 21.66,
    "duration": 6.72
  },
  {
    "text": "web pages or so on that are related to",
    "start": 24.96,
    "duration": 5.7
  },
  {
    "text": "our particular question and we're also",
    "start": 28.38,
    "duration": 4.92
  },
  {
    "text": "going to be able to use something called",
    "start": 30.66,
    "duration": 5.7
  },
  {
    "text": "a generator model to generate a human",
    "start": 33.3,
    "duration": 6.8
  },
  {
    "text": "natural language answer to our question",
    "start": 36.36,
    "duration": 6.42
  },
  {
    "text": "based on these documents that we've",
    "start": 40.1,
    "duration": 5.32
  },
  {
    "text": "retrieved from an external source so we",
    "start": 42.78,
    "duration": 6.299
  },
  {
    "text": "can think of it as a GPT model that is",
    "start": 45.42,
    "duration": 6.72
  },
  {
    "text": "answering our questions but if gbt was",
    "start": 49.079,
    "duration": 5.401
  },
  {
    "text": "also giving us the sources of the",
    "start": 52.14,
    "duration": 3.84
  },
  {
    "text": "information that it was answering",
    "start": 54.48,
    "duration": 3.419
  },
  {
    "text": "questions based on so let's jump",
    "start": 55.98,
    "duration": 4.62
  },
  {
    "text": "straight into just understanding why",
    "start": 57.899,
    "duration": 4.32
  },
  {
    "text": "exactly that we're going to be building",
    "start": 60.6,
    "duration": 4.04
  },
  {
    "text": "so we're going to start with all of our",
    "start": 62.219,
    "duration": 5.341
  },
  {
    "text": "documents our text or whatever it is",
    "start": 64.64,
    "duration": 4.659
  },
  {
    "text": "we're going to be using in our case",
    "start": 67.56,
    "duration": 4.739
  },
  {
    "text": "we're going to be using text from",
    "start": 69.299,
    "duration": 5.101
  },
  {
    "text": "Wikipedia so we're going to take all of",
    "start": 72.299,
    "duration": 5.701
  },
  {
    "text": "this and we're going to encode it using",
    "start": 74.4,
    "duration": 6.18
  },
  {
    "text": "what's called a retriever model so it's",
    "start": 78.0,
    "duration": 5.46
  },
  {
    "text": "called a retriever and what that will",
    "start": 80.58,
    "duration": 6.96
  },
  {
    "text": "give us is a ton of these vectors where",
    "start": 83.46,
    "duration": 7.56
  },
  {
    "text": "each Vector represents like a segment of",
    "start": 87.54,
    "duration": 4.8
  },
  { "text": "our text", "start": 91.02, "duration": 3.9 },
  {
    "text": "so for example maybe we might have this",
    "start": 92.34,
    "duration": 4.98
  },
  {
    "text": "little segment here followed by",
    "start": 94.92,
    "duration": 5.879
  },
  {
    "text": "this segment and so on we're going to",
    "start": 97.32,
    "duration": 6.659
  },
  {
    "text": "take all of those vector embeddings and",
    "start": 100.799,
    "duration": 4.981
  },
  {
    "text": "we're going to put them into a vector",
    "start": 103.979,
    "duration": 5.721
  },
  { "text": "database over here", "start": 105.78, "duration": 3.92 },
  {
    "text": "now we're going to be using pine cone",
    "start": 109.86,
    "duration": 4.079
  },
  {
    "text": "for this so what we'll do is just put",
    "start": 111.479,
    "duration": 5.1
  },
  {
    "text": "everything in Pine Cone and at that",
    "start": 113.939,
    "duration": 5.401
  },
  {
    "text": "point we've actually built the retrieval",
    "start": 116.579,
    "duration": 4.921
  },
  {
    "text": "pipeline we don't have the generative",
    "start": 119.34,
    "duration": 4.62
  },
  {
    "text": "part of it yet but we'll do a retrieval",
    "start": 121.5,
    "duration": 5.28
  },
  {
    "text": "pipeline so then what we can do is ask a",
    "start": 123.96,
    "duration": 5.579
  },
  {
    "text": "question so ask a question over here it",
    "start": 126.78,
    "duration": 4.98
  },
  {
    "text": "will be in natural language and what",
    "start": 129.539,
    "duration": 4.501
  },
  {
    "text": "we'll do with that is actually also take",
    "start": 131.76,
    "duration": 4.44
  },
  {
    "text": "that into the retriever model and that",
    "start": 134.04,
    "duration": 6.0
  },
  {
    "text": "will output we'll maybe we'll output it",
    "start": 136.2,
    "duration": 6.899
  },
  {
    "text": "over here that will output a single",
    "start": 140.04,
    "duration": 6.24
  },
  {
    "text": "query vector okay or question Vector",
    "start": 143.099,
    "duration": 5.28
  },
  {
    "text": "that would then be passed into pinecen",
    "start": 146.28,
    "duration": 4.62
  },
  {
    "text": "here which will compare that query",
    "start": 148.379,
    "duration": 5.101
  },
  {
    "text": "Vector to all of the previously encoded",
    "start": 150.9,
    "duration": 4.979
  },
  {
    "text": "vectors and it will return a few of",
    "start": 153.48,
    "duration": 4.2
  },
  {
    "text": "those that are the most relevant to our",
    "start": 155.879,
    "duration": 4.08
  },
  {
    "text": "particular query Vector so it will bring",
    "start": 157.68,
    "duration": 4.44
  },
  {
    "text": "these out and then we say okay these",
    "start": 159.959,
    "duration": 4.201
  },
  {
    "text": "three items are the most relevant to",
    "start": 162.12,
    "duration": 4.199
  },
  {
    "text": "your particular query and it's basing",
    "start": 164.16,
    "duration": 5.159
  },
  {
    "text": "those on look at the concept or the idea",
    "start": 166.319,
    "duration": 4.621
  },
  {
    "text": "behind the language being used it's not",
    "start": 169.319,
    "duration": 4.441
  },
  {
    "text": "basing them on matching particular terms",
    "start": 170.94,
    "duration": 4.32
  },
  {
    "text": "like keyword matching or anything like",
    "start": 173.76,
    "duration": 3.119
  },
  {
    "text": "that it's actually basing it on the",
    "start": 175.26,
    "duration": 4.8
  },
  {
    "text": "semantic understanding of the question",
    "start": 176.879,
    "duration": 7.021
  },
  {
    "text": "and of the answers and of the relevant",
    "start": 180.06,
    "duration": 6.899
  },
  {
    "text": "documents so we would take these and",
    "start": 183.9,
    "duration": 6.36
  },
  {
    "text": "we'll bring them over here now over here",
    "start": 186.959,
    "duration": 4.621
  },
  {
    "text": "we're going to have what's called a",
    "start": 190.26,
    "duration": 3.899
  },
  {
    "text": "generator model so the generator model",
    "start": 191.58,
    "duration": 5.82
  },
  {
    "text": "it can be a lot of different things one",
    "start": 194.159,
    "duration": 5.22
  },
  {
    "text": "example that I kind of briefly mentioned",
    "start": 197.4,
    "duration": 3.96
  },
  {
    "text": "is it could actually be something like",
    "start": 199.379,
    "duration": 3.961
  },
  { "text": "gpt3", "start": 201.36, "duration": 4.44 },
  {
    "text": "so you can have gpt3 here we're going to",
    "start": 203.34,
    "duration": 5.16
  },
  {
    "text": "be using another one or another model",
    "start": 205.8,
    "duration": 4.859
  },
  {
    "text": "called Bart that will generate",
    "start": 208.5,
    "duration": 5.04
  },
  {
    "text": "everything for us just because this is",
    "start": 210.659,
    "duration": 4.981
  },
  {
    "text": "open source and we can just run it in",
    "start": 213.54,
    "duration": 4.559
  },
  {
    "text": "our code love notebook but you can use",
    "start": 215.64,
    "duration": 4.86
  },
  {
    "text": "gpg 3 you can use to go hey you cannot",
    "start": 218.099,
    "duration": 4.081
  },
  {
    "text": "use all these different types of models",
    "start": 220.5,
    "duration": 4.2
  },
  {
    "text": "depending on what is you're wanting to",
    "start": 222.18,
    "duration": 6.6
  },
  {
    "text": "do so we'd pass those relevant contacts",
    "start": 224.7,
    "duration": 6.06
  },
  {
    "text": "or documents whatever you like to call",
    "start": 228.78,
    "duration": 4.56
  },
  {
    "text": "them we pass those into our generator",
    "start": 230.76,
    "duration": 4.92
  },
  {
    "text": "model alongside that we also want to",
    "start": 233.34,
    "duration": 4.5
  },
  {
    "text": "pass in the question the original",
    "start": 235.68,
    "duration": 3.32
  },
  { "text": "question", "start": 237.84, "duration": 5.1 },
  {
    "text": "one thing that I missed here is actually",
    "start": 239.0,
    "duration": 6.04
  },
  { "text": "here", "start": 242.94, "duration": 4.4 },
  { "text": "foreign", "start": 245.04, "duration": 2.3 },
  {
    "text": "back into their original text format",
    "start": 250.64,
    "duration": 7.96
  },
  {
    "text": "which we've stored in Pinecone so that",
    "start": 255.299,
    "duration": 6.0
  },
  {
    "text": "will actually be the text and the same",
    "start": 258.6,
    "duration": 3.72
  },
  {
    "text": "with the query so we're going to have",
    "start": 261.299,
    "duration": 2.881
  },
  {
    "text": "the query and the context and we're",
    "start": 262.32,
    "duration": 3.9
  },
  {
    "text": "going to feeding them into generator",
    "start": 264.18,
    "duration": 4.86
  },
  {
    "text": "and that will then output as an answer",
    "start": 266.22,
    "duration": 7.02
  },
  {
    "text": "in natural language format so let's",
    "start": 269.04,
    "duration": 6.12
  },
  {
    "text": "actually jump straight into the code for",
    "start": 273.24,
    "duration": 4.08
  },
  {
    "text": "building all of this so we're going to",
    "start": 275.16,
    "duration": 4.979
  },
  {
    "text": "be working from this example over on the",
    "start": 277.32,
    "duration": 6.659
  },
  {
    "text": "pine cone dots so it's pancone IO dots",
    "start": 280.139,
    "duration": 6.421
  },
  {
    "text": "abstractive question answering",
    "start": 283.979,
    "duration": 4.561
  },
  {
    "text": "and there'll be a link in the video as",
    "start": 286.56,
    "duration": 3.78
  },
  {
    "text": "well and what we want to do is just",
    "start": 288.54,
    "duration": 4.32
  },
  {
    "text": "opening collab over here that will open",
    "start": 290.34,
    "duration": 5.34
  },
  {
    "text": "this so let's get started we need to",
    "start": 292.86,
    "duration": 6.0
  },
  {
    "text": "install any dependencies so in here we",
    "start": 295.68,
    "duration": 5.64
  },
  {
    "text": "have data sets pineco and sentence",
    "start": 298.86,
    "duration": 5.339
  },
  {
    "text": "Transformers and pytorch and we'll jump",
    "start": 301.32,
    "duration": 5.04
  },
  {
    "text": "into what each one of those does pretty",
    "start": 304.199,
    "duration": 4.861
  },
  {
    "text": "soon okay once that is installed we come",
    "start": 306.36,
    "duration": 4.559
  },
  {
    "text": "down here and we're going to just load",
    "start": 309.06,
    "duration": 4.5
  },
  {
    "text": "and prepare our data set so we're taking",
    "start": 310.919,
    "duration": 5.34
  },
  {
    "text": "these Wikipedia Snippets date step and",
    "start": 313.56,
    "duration": 4.32
  },
  {
    "text": "this is coming from the hug and face",
    "start": 316.259,
    "duration": 4.681
  },
  {
    "text": "data sets Hub so we're loading it like",
    "start": 317.88,
    "duration": 7.2
  },
  {
    "text": "this and it's a pretty big data set so",
    "start": 320.94,
    "duration": 7.199
  },
  {
    "text": "we're actually streaming that data by",
    "start": 325.08,
    "duration": 4.86
  },
  {
    "text": "saying streaming equals true I think",
    "start": 328.139,
    "duration": 3.961
  },
  {
    "text": "it's nine gigabytes so this will just",
    "start": 329.94,
    "duration": 4.319
  },
  {
    "text": "allow us to load what we're using right",
    "start": 332.1,
    "duration": 3.9
  },
  {
    "text": "now rather than loading the full thing",
    "start": 334.259,
    "duration": 3.78
  },
  {
    "text": "in memory at once and then we Shuffle",
    "start": 336.0,
    "duration": 5.34
  },
  {
    "text": "that data set randomly so we we're using",
    "start": 338.039,
    "duration": 4.921
  },
  {
    "text": "a seat here just so you can replicate",
    "start": 341.34,
    "duration": 4.919
  },
  {
    "text": "what I'm doing here let me run this and",
    "start": 342.96,
    "duration": 5.22
  },
  {
    "text": "then we'll come down here and we can",
    "start": 346.259,
    "duration": 5.041
  },
  {
    "text": "just show the first item or the first",
    "start": 348.18,
    "duration": 5.76
  },
  {
    "text": "document from the data set so we just",
    "start": 351.3,
    "duration": 4.02
  },
  {
    "text": "iterating through it we take the next",
    "start": 353.94,
    "duration": 4.86
  },
  {
    "text": "item and we can see we have the ID and",
    "start": 355.32,
    "duration": 4.98
  },
  {
    "text": "we saw and then where you know where",
    "start": 358.8,
    "duration": 4.86
  },
  {
    "text": "where the text is actually being pulled",
    "start": 360.3,
    "duration": 6.54
  },
  {
    "text": "from and we have article title section",
    "start": 363.66,
    "duration": 5.58
  },
  {
    "text": "title and then we have the passage tips",
    "start": 366.84,
    "duration": 4.56
  },
  {
    "text": "okay so this is the the document or the",
    "start": 369.24,
    "duration": 4.679
  },
  {
    "text": "context and this is what we're going to",
    "start": 371.4,
    "duration": 3.84
  },
  {
    "text": "be encoding so this is what we're going",
    "start": 373.919,
    "duration": 4.081
  },
  {
    "text": "to be encoding and storing in our Vector",
    "start": 375.24,
    "duration": 6.239
  },
  {
    "text": "database so what I'm going to do here is",
    "start": 378.0,
    "duration": 6.84
  },
  {
    "text": "actually filter for only the documents",
    "start": 381.479,
    "duration": 6.181
  },
  {
    "text": "that have history in the section title",
    "start": 384.84,
    "duration": 5.34
  },
  {
    "text": "here so basically we just want history",
    "start": 387.66,
    "duration": 6.42
  },
  {
    "text": "related documents so we do that now we",
    "start": 390.18,
    "duration": 6.12
  },
  {
    "text": "can't check how many items we have there",
    "start": 394.08,
    "duration": 3.899
  },
  {
    "text": "because we're using the streaming",
    "start": 396.3,
    "duration": 4.019
  },
  {
    "text": "feature so that will just essentially",
    "start": 397.979,
    "duration": 3.961
  },
  {
    "text": "stream everything and if it sees history",
    "start": 400.319,
    "duration": 3.961
  },
  {
    "text": "it will lay through if not it will not",
    "start": 401.94,
    "duration": 4.5
  },
  {
    "text": "let through but they're quite a few",
    "start": 404.28,
    "duration": 5.52
  },
  {
    "text": "teeth passages in there so we're just",
    "start": 406.44,
    "duration": 5.58
  },
  {
    "text": "going to filter out or we're going to",
    "start": 409.8,
    "duration": 5.28
  },
  {
    "text": "choose the first 50 000 of those which",
    "start": 412.02,
    "duration": 5.58
  },
  { "text": "is quite a bit", "start": 415.08, "duration": 5.22 },
  {
    "text": "now one thing I should make you aware of",
    "start": 417.6,
    "duration": 5.76
  },
  {
    "text": "here is in your runtime just it should",
    "start": 420.3,
    "duration": 5.76
  },
  {
    "text": "be GPU anyway but in case it's not here",
    "start": 423.36,
    "duration": 4.339
  },
  { "text": "you can set", "start": 426.06, "duration": 5.1 },
  {
    "text": "your Hardware to use a GPU if it's on",
    "start": 427.699,
    "duration": 5.021
  },
  {
    "text": "none it means you're using CPU and it",
    "start": 431.16,
    "duration": 2.58
  },
  {
    "text": "will be a lot slower when we're",
    "start": 432.72,
    "duration": 3.66
  },
  {
    "text": "embedding everything later on so we do",
    "start": 433.74,
    "duration": 6.38
  },
  {
    "text": "want to make sure that we're using GPU",
    "start": 436.38,
    "duration": 3.74
  },
  {
    "text": "okay so after that has completed we have",
    "start": 441.0,
    "duration": 5.099
  },
  { "text": "our 50", "start": 444.9, "duration": 5.4 },
  {
    "text": "000 documents all with history in the",
    "start": 446.099,
    "duration": 6.241
  },
  {
    "text": "section title so if we take a look at",
    "start": 450.3,
    "duration": 3.119
  },
  { "text": "the head here", "start": 452.34, "duration": 3.479 },
  {
    "text": "we can see that all knows and don't all",
    "start": 453.419,
    "duration": 5.34
  },
  {
    "text": "say history specifically but they have",
    "start": 455.819,
    "duration": 5.521
  },
  {
    "text": "history at least in the title like here",
    "start": 458.759,
    "duration": 6.601
  },
  {
    "text": "okay so what we're going to do now is",
    "start": 461.34,
    "duration": 7.68
  },
  {
    "text": "we'll need to embed and index all of",
    "start": 465.36,
    "duration": 5.94
  },
  {
    "text": "these passages here or embed and sort",
    "start": 469.02,
    "duration": 4.2
  },
  {
    "text": "all of them so to do that we're going to",
    "start": 471.3,
    "duration": 4.08
  },
  {
    "text": "we'll need to initialize the pine cone",
    "start": 473.22,
    "duration": 3.9
  },
  {
    "text": "index but I'm going to do that after",
    "start": 475.38,
    "duration": 4.2
  },
  {
    "text": "initializing the retriever model so I'm",
    "start": 477.12,
    "duration": 4.68
  },
  {
    "text": "going to scroll down to here come to the",
    "start": 479.58,
    "duration": 3.6
  },
  {
    "text": "retrieve model and we're going to be",
    "start": 481.8,
    "duration": 3.54
  },
  {
    "text": "using this Flex sentence embeddings or",
    "start": 483.18,
    "duration": 6.959
  },
  {
    "text": "data sets V3 mpnet base model so this is",
    "start": 485.34,
    "duration": 7.799
  },
  {
    "text": "basically one of the best sentence",
    "start": 490.139,
    "duration": 4.62
  },
  {
    "text": "transform models you can use for",
    "start": 493.139,
    "duration": 4.201
  },
  {
    "text": "basically anything so that's why it has",
    "start": 494.759,
    "duration": 4.921
  },
  {
    "text": "all here it has been trained on I think",
    "start": 497.34,
    "duration": 5.639
  },
  {
    "text": "a billion sentence pairs so it's a",
    "start": 499.68,
    "duration": 5.82
  },
  {
    "text": "pretty good model to try and use",
    "start": 502.979,
    "duration": 4.5
  },
  {
    "text": "whenever you're not sure which model to",
    "start": 505.5,
    "duration": 4.919
  },
  {
    "text": "use so we initialize that okay it might",
    "start": 507.479,
    "duration": 4.98
  },
  { "text": "take a moment to download", "start": 510.419, "duration": 5.101 },
  {
    "text": "okay and then one thing we will want to",
    "start": 512.459,
    "duration": 8.341
  },
  {
    "text": "do is make sure we move this to a GPU so",
    "start": 515.52,
    "duration": 8.22
  },
  {
    "text": "actually what we need to do is import",
    "start": 520.8,
    "duration": 4.38
  },
  { "text": "torch", "start": 523.74, "duration": 5.34 },
  {
    "text": "now I want to say device equals Cuda",
    "start": 525.18,
    "duration": 6.36
  },
  { "text": "if torch", "start": 529.08, "duration": 5.16 },
  {
    "text": "Cuda is available so this is saying if",
    "start": 531.54,
    "duration": 4.979
  },
  { "text": "there's a cooler enabled GPU", "start": 534.24, "duration": 4.62 },
  { "text": "set the device to that", "start": 536.519, "duration": 5.221 },
  {
    "text": "otherwise we're going to use CPU",
    "start": 538.86,
    "duration": 5.82
  },
  {
    "text": "okay now we can see what the device is",
    "start": 541.74,
    "duration": 5.039
  },
  {
    "text": "and actually rather than moving the",
    "start": 544.68,
    "duration": 4.08
  },
  {
    "text": "retriever to that device I'm going to",
    "start": 546.779,
    "duration": 4.141
  },
  {
    "text": "come back up to the initialization here",
    "start": 548.76,
    "duration": 4.259
  },
  {
    "text": "and I'm going to initialize it on that",
    "start": 550.92,
    "duration": 5.9
  },
  {
    "text": "device to start with so like this okay",
    "start": 553.019,
    "duration": 7.44
  },
  {
    "text": "now an important thing to note here is",
    "start": 556.82,
    "duration": 4.9
  },
  {
    "text": "that we have the word embedding",
    "start": 560.459,
    "duration": 4.201
  },
  { "text": "Dimension seven six eight", "start": 561.72, "duration": 5.78 },
  {
    "text": "so remember that and we'll come up here",
    "start": 564.66,
    "duration": 5.4
  },
  {
    "text": "and we will initialize our pine cone",
    "start": 567.5,
    "duration": 5.2
  },
  {
    "text": "index so the first thing we need to do",
    "start": 570.06,
    "duration": 4.26
  },
  {
    "text": "is connect to our pine cone environment",
    "start": 572.7,
    "duration": 3.96
  },
  {
    "text": "so we need an API key for that which is",
    "start": 574.32,
    "duration": 6.06
  },
  {
    "text": "free so to get that we need to go to",
    "start": 576.66,
    "duration": 6.48
  },
  { "text": "app.pinecone", "start": 580.38, "duration": 6.12 },
  {
    "text": "dot IO I want to say we will need to",
    "start": 583.14,
    "duration": 6.96
  },
  {
    "text": "sign up or log in so I'm going to log in",
    "start": 586.5,
    "duration": 5.94
  },
  {
    "text": "and once we've done that we'll just get",
    "start": 590.1,
    "duration": 5.82
  },
  {
    "text": "a little loading screen here and then we",
    "start": 592.44,
    "duration": 6.36
  },
  {
    "text": "should find something like this so on",
    "start": 595.92,
    "duration": 5.039
  },
  { "text": "the top left up here", "start": 598.8, "duration": 4.38 },
  {
    "text": "you have your organization and then you",
    "start": 600.959,
    "duration": 5.82
  },
  {
    "text": "have projects so one of those should say",
    "start": 603.18,
    "duration": 6.06
  },
  {
    "text": "like your name and default project so",
    "start": 606.779,
    "duration": 4.921
  },
  {
    "text": "I'm going to go over to that and in here",
    "start": 609.24,
    "duration": 5.34
  },
  {
    "text": "I just have a list of the indexes that I",
    "start": 611.7,
    "duration": 4.56
  },
  {
    "text": "currently have running now I think",
    "start": 614.58,
    "duration": 4.56
  },
  {
    "text": "abstractive question answering is not in",
    "start": 616.26,
    "duration": 4.86
  },
  {
    "text": "there so what I'm going to do is we're",
    "start": 619.14,
    "duration": 3.84
  },
  {
    "text": "going to have to create it so we come",
    "start": 621.12,
    "duration": 4.44
  },
  {
    "text": "over to API keys on the left here we",
    "start": 622.98,
    "duration": 5.64
  },
  { "text": "copy the API key value", "start": 625.56, "duration": 5.219 },
  {
    "text": "come over to here and then we would just",
    "start": 628.62,
    "duration": 4.62
  },
  {
    "text": "paste it into here I'm going to go and",
    "start": 630.779,
    "duration": 5.161
  },
  {
    "text": "paste mine into a new variable so mine",
    "start": 633.24,
    "duration": 5.64
  },
  {
    "text": "is sword in a new variable called API",
    "start": 635.94,
    "duration": 3.66
  },
  { "text": "key", "start": 638.88, "duration": 4.28 },
  { "text": "so I initialize with that", "start": 639.6, "duration": 3.56 },
  {
    "text": "and what we're going to do is create a",
    "start": 644.3,
    "duration": 3.52
  },
  {
    "text": "new index we're going to call it",
    "start": 646.74,
    "duration": 4.56
  },
  {
    "text": "abstractive question answering and we",
    "start": 647.82,
    "duration": 5.22
  },
  {
    "text": "are going to say if that index name does",
    "start": 651.3,
    "duration": 5.159
  },
  {
    "text": "not exist then we create it now I",
    "start": 653.04,
    "duration": 5.76
  },
  {
    "text": "remember I said to remember that",
    "start": 656.459,
    "duration": 5.401
  },
  {
    "text": "dimensionality at number 768 before this",
    "start": 658.8,
    "duration": 5.52
  },
  {
    "text": "is why because it's here we need that",
    "start": 661.86,
    "duration": 5.34
  },
  {
    "text": "number to Align this number here to a",
    "start": 664.32,
    "duration": 5.579
  },
  {
    "text": "line with the embedding dimensionality",
    "start": 667.2,
    "duration": 5.46
  },
  {
    "text": "of our retriever model we can also check",
    "start": 669.899,
    "duration": 6.481
  },
  {
    "text": "that using this so Retriever get",
    "start": 672.66,
    "duration": 6.419
  },
  {
    "text": "sentence embedding dimension",
    "start": 676.38,
    "duration": 5.579
  },
  {
    "text": "like so and we get 768 so we can",
    "start": 679.079,
    "duration": 5.521
  },
  {
    "text": "actually take this and place it in here",
    "start": 681.959,
    "duration": 4.681
  },
  {
    "text": "rather than hard coding it metric",
    "start": 684.6,
    "duration": 6.479
  },
  {
    "text": "because the embedding vectors are",
    "start": 686.64,
    "duration": 8.4
  },
  {
    "text": "normalized as we can see here we can",
    "start": 691.079,
    "duration": 5.521
  },
  {
    "text": "actually use either dot product or",
    "start": 695.04,
    "duration": 3.6
  },
  {
    "text": "cosine similarity here we're going to",
    "start": 696.6,
    "duration": 4.02
  },
  {
    "text": "just stick cosine similarity and that",
    "start": 698.64,
    "duration": 4.08
  },
  {
    "text": "will just take a moment for the index to",
    "start": 700.62,
    "duration": 3.48
  },
  { "text": "be created", "start": 702.72, "duration": 3.239 },
  {
    "text": "okay once we have created it we will",
    "start": 704.1,
    "duration": 4.08
  },
  {
    "text": "move on to this which is just connecting",
    "start": 705.959,
    "duration": 6.361
  },
  {
    "text": "to our new index so let's scroll down",
    "start": 708.18,
    "duration": 6.12
  },
  {
    "text": "and we will come down to the generating",
    "start": 712.32,
    "duration": 4.56
  },
  {
    "text": "embeddings and upsetting so what we're",
    "start": 714.3,
    "duration": 4.44
  },
  {
    "text": "going to do here is in batches of 64",
    "start": 716.88,
    "duration": 6.0
  },
  {
    "text": "we're going to extract our passage text",
    "start": 718.74,
    "duration": 6.9
  },
  {
    "text": "so we'll have 64 of these passages",
    "start": 722.88,
    "duration": 5.16
  },
  {
    "text": "although one time and we're going to",
    "start": 725.64,
    "duration": 4.139
  },
  {
    "text": "encode them all using our retrieve model",
    "start": 728.04,
    "duration": 3.18
  },
  {
    "text": "then what we're going to do is get",
    "start": 729.779,
    "duration": 4.981
  },
  {
    "text": "metadata so that is simply the",
    "start": 731.22,
    "duration": 6.5
  },
  {
    "text": "the text that we have in here so if I",
    "start": 734.76,
    "duration": 7.98
  },
  {
    "text": "show you an example we have take this",
    "start": 737.72,
    "duration": 7.96
  },
  {
    "text": "and then the DF and we're going to take",
    "start": 742.74,
    "duration": 6.96
  },
  {
    "text": "first a few items and paste that",
    "start": 745.68,
    "duration": 5.159
  },
  {
    "text": "so we're basically going to do this",
    "start": 749.7,
    "duration": 3.12
  },
  {
    "text": "we're going to take all of that",
    "start": 750.839,
    "duration": 4.801
  },
  {
    "text": "data that we have now data frame and for",
    "start": 752.82,
    "duration": 5.04
  },
  {
    "text": "each one of our vectors so first one",
    "start": 755.64,
    "duration": 4.379
  },
  {
    "text": "will be this we're going to attach that",
    "start": 757.86,
    "duration": 4.8
  },
  {
    "text": "metadata to the vector and then here",
    "start": 760.019,
    "duration": 5.041
  },
  {
    "text": "would create some unique IDs just count",
    "start": 762.66,
    "duration": 4.799
  },
  {
    "text": "uh we could actually use the IDS",
    "start": 765.06,
    "duration": 5.519
  },
  {
    "text": "themselves but this is just easier and",
    "start": 767.459,
    "duration": 4.921
  },
  {
    "text": "we're going to add all those to a upset",
    "start": 770.579,
    "duration": 4.741
  },
  {
    "text": "list which is just a list that contains",
    "start": 772.38,
    "duration": 5.82
  },
  {
    "text": "two boards containing a each ID the",
    "start": 775.32,
    "duration": 4.68
  },
  {
    "text": "vector embedding and the metadata",
    "start": 778.2,
    "duration": 3.6
  },
  {
    "text": "related to that embedding and then we",
    "start": 780.0,
    "duration": 3.899
  },
  {
    "text": "upset all of that so basically inside",
    "start": 781.8,
    "duration": 5.42
  },
  {
    "text": "all into the pine cone Vector database",
    "start": 783.899,
    "duration": 6.18
  },
  {
    "text": "then at the end here we're just going to",
    "start": 787.22,
    "duration": 4.299
  },
  {
    "text": "check that we have all those vectors in",
    "start": 790.079,
    "duration": 3.661
  },
  {
    "text": "the index and you can see here that it",
    "start": 791.519,
    "duration": 5.101
  },
  {
    "text": "actually brought through five fifty",
    "start": 793.74,
    "duration": 4.92
  },
  {
    "text": "thousand and one so maybe there's a",
    "start": 796.62,
    "duration": 4.56
  },
  {
    "text": "duplicate in there I'm not too sure but",
    "start": 798.66,
    "duration": 5.34
  },
  {
    "text": "we have all of those in there so I can",
    "start": 801.18,
    "duration": 4.8
  },
  {
    "text": "try running this but it's basically just",
    "start": 804.0,
    "duration": 4.92
  },
  {
    "text": "going to start from start again so you",
    "start": 805.98,
    "duration": 5.46
  },
  {
    "text": "can see here I'm not going to wait until",
    "start": 808.92,
    "duration": 5.34
  },
  {
    "text": "the end of that because it will take a",
    "start": 811.44,
    "duration": 5.1
  },
  {
    "text": "little bit of time even when we're using",
    "start": 814.26,
    "duration": 4.86
  },
  {
    "text": "a GPU on collab although actually not",
    "start": 816.54,
    "duration": 4.56
  },
  {
    "text": "too long anyway I'm going to stop that",
    "start": 819.12,
    "duration": 4.5
  },
  {
    "text": "and we'll just move straight on to the",
    "start": 821.1,
    "duration": 4.919
  },
  {
    "text": "generator and we can at least just see",
    "start": 823.62,
    "duration": 6.12
  },
  {
    "text": "from the pass runs at what it would be",
    "start": 826.019,
    "duration": 5.341
  },
  {
    "text": "doing so the first thing we would do",
    "start": 829.74,
    "duration": 4.68
  },
  {
    "text": "here is initialize the tokenizer and the",
    "start": 831.36,
    "duration": 5.219
  },
  {
    "text": "model for our generator model and we're",
    "start": 834.42,
    "duration": 5.159
  },
  {
    "text": "using a spot lfqa which is long-formal",
    "start": 836.579,
    "duration": 5.94
  },
  {
    "text": "question hand string model okay so if",
    "start": 839.579,
    "duration": 5.041
  },
  {
    "text": "you come up here we'll explain a little",
    "start": 842.519,
    "duration": 4.141
  },
  {
    "text": "bit of what this model is so using the",
    "start": 844.62,
    "duration": 5.1
  },
  {
    "text": "explain lycam 5 bar model which is just",
    "start": 846.66,
    "duration": 5.34
  },
  {
    "text": "a sequence sequence model which has been",
    "start": 849.72,
    "duration": 5.1
  },
  {
    "text": "trained using at Spain like M5 data set",
    "start": 852.0,
    "duration": 5.82
  },
  {
    "text": "which is from Reddit and if we come down",
    "start": 854.82,
    "duration": 4.259
  },
  {
    "text": "here we can see the format that we're",
    "start": 857.82,
    "duration": 3.78
  },
  {
    "text": "going to be putting all of our text into",
    "start": 859.079,
    "duration": 4.2
  },
  {
    "text": "this model so we're going to have our",
    "start": 861.6,
    "duration": 4.32
  },
  {
    "text": "question which can be what we type we",
    "start": 863.279,
    "duration": 5.041
  },
  {
    "text": "say like what is a sonic boom and then",
    "start": 865.92,
    "duration": 5.64
  },
  {
    "text": "that's followed by context and then with",
    "start": 868.32,
    "duration": 6.84
  },
  {
    "text": "each passage we proceed it with a p",
    "start": 871.56,
    "duration": 5.399
  },
  {
    "text": "token like this and then we have the",
    "start": 875.16,
    "duration": 4.08
  },
  {
    "text": "passage and then P token another passage",
    "start": 876.959,
    "duration": 4.5
  },
  {
    "text": "and basically the model has been trained",
    "start": 879.24,
    "duration": 4.56
  },
  {
    "text": "to read this sort of format and then",
    "start": 881.459,
    "duration": 5.88
  },
  {
    "text": "generate a natural language answer based",
    "start": 883.8,
    "duration": 6.36
  },
  {
    "text": "on this question and based on this",
    "start": 887.339,
    "duration": 4.74
  },
  {
    "text": "information that we have provided it",
    "start": 890.16,
    "duration": 5.28
  },
  {
    "text": "with so we come down here we would",
    "start": 892.079,
    "duration": 6.301
  },
  {
    "text": "initialize it like that and then we're",
    "start": 895.44,
    "duration": 5.699
  },
  {
    "text": "just going to create these to helper",
    "start": 898.38,
    "duration": 4.92
  },
  {
    "text": "functions so this is just to help us",
    "start": 901.139,
    "duration": 4.621
  },
  {
    "text": "query Pinecone so given a particular",
    "start": 903.3,
    "duration": 6.659
  },
  {
    "text": "query we encode it so from text to a",
    "start": 905.76,
    "duration": 7.139
  },
  {
    "text": "vector embedding or the query embedding",
    "start": 909.959,
    "duration": 5.841
  },
  {
    "text": "is what we usually call it we query",
    "start": 912.899,
    "duration": 6.3
  },
  {
    "text": "Pinecone like this this will return K",
    "start": 915.8,
    "duration": 8.26
  },
  {
    "text": "many passages and it would return these",
    "start": 919.199,
    "duration": 7.681
  },
  {
    "text": "what what we call the contacts or the",
    "start": 924.06,
    "duration": 5.48
  },
  {
    "text": "passages or something along those lines",
    "start": 926.88,
    "duration": 5.04
  },
  {
    "text": "one thing that is pretty important here",
    "start": 929.54,
    "duration": 3.88
  },
  {
    "text": "is that we include the metadata because",
    "start": 931.92,
    "duration": 4.08
  },
  {
    "text": "that includes the human readable text of",
    "start": 933.42,
    "duration": 3.84
  },
  {
    "text": "those pastures that we're going to be",
    "start": 936.0,
    "duration": 3.3
  },
  {
    "text": "feeding in and why do we need that",
    "start": 937.26,
    "duration": 3.84
  },
  {
    "text": "because we are going to be formatting",
    "start": 939.3,
    "duration": 4.14
  },
  {
    "text": "them in this string which is like what I",
    "start": 941.1,
    "duration": 5.34
  },
  {
    "text": "showed you before we have the",
    "start": 943.44,
    "duration": 5.399
  },
  {
    "text": "so the context here which is going to be",
    "start": 946.44,
    "duration": 5.82
  },
  {
    "text": "the P token followed by the passage and",
    "start": 948.839,
    "duration": 5.581
  },
  {
    "text": "then we concatenate all those together",
    "start": 952.26,
    "duration": 4.8
  },
  { "text": "and then what we would do is", "start": 954.42, "duration": 4.5 },
  {
    "text": "create that format that you saw before",
    "start": 957.06,
    "duration": 3.54
  },
  {
    "text": "with the question followed by the",
    "start": 958.92,
    "duration": 3.3
  },
  {
    "text": "question and the context followed by",
    "start": 960.6,
    "duration": 4.14
  },
  {
    "text": "those contacts with the p tokens in the",
    "start": 962.22,
    "duration": 5.34
  },
  {
    "text": "in the middle or preceding each one so",
    "start": 964.74,
    "duration": 5.219
  },
  {
    "text": "with those help functions we then move",
    "start": 967.56,
    "duration": 4.86
  },
  {
    "text": "on to our query so we have our query",
    "start": 969.959,
    "duration": 5.161
  },
  {
    "text": "when's the first electric power system",
    "start": 972.42,
    "duration": 5.039
  },
  {
    "text": "built we can query pine cone and that",
    "start": 975.12,
    "duration": 4.079
  },
  {
    "text": "will return these matches here so this",
    "start": 977.459,
    "duration": 4.44
  },
  {
    "text": "is the response directly from Pinecone",
    "start": 979.199,
    "duration": 5.101
  },
  {
    "text": "and we see that we have the passage text",
    "start": 981.899,
    "duration": 5.041
  },
  {
    "text": "and we have some I think relevant",
    "start": 984.3,
    "duration": 4.62
  },
  {
    "text": "passages in there so this is just",
    "start": 986.94,
    "duration": 5.1
  },
  {
    "text": "returning just returning one here",
    "start": 988.92,
    "duration": 6.02
  },
  {
    "text": "we use pretty print here so that we can",
    "start": 992.04,
    "duration": 5.58
  },
  {
    "text": "more nicely visualize everything or",
    "start": 994.94,
    "duration": 4.72
  },
  {
    "text": "print everything and then what we want",
    "start": 997.62,
    "duration": 5.76
  },
  {
    "text": "to do is query or format our query so we",
    "start": 999.66,
    "duration": 6.06
  },
  {
    "text": "have our query which is a question we",
    "start": 1003.38,
    "duration": 3.899
  },
  {
    "text": "just asked up here one's first electric",
    "start": 1005.72,
    "duration": 3.6
  },
  {
    "text": "power system built and then we also have",
    "start": 1007.279,
    "duration": 5.401
  },
  {
    "text": "what we return from Pinecone okay we and",
    "start": 1009.32,
    "duration": 6.24
  },
  {
    "text": "then we print what we get from there or",
    "start": 1012.68,
    "duration": 5.64
  },
  {
    "text": "what we will be producing so we have the",
    "start": 1015.56,
    "duration": 4.38
  },
  {
    "text": "question and you can see that same",
    "start": 1018.32,
    "duration": 4.019
  },
  {
    "text": "format that you saw before and then you",
    "start": 1019.94,
    "duration": 4.619
  },
  {
    "text": "have contacts and you have the P token",
    "start": 1022.339,
    "duration": 4.801
  },
  {
    "text": "followed by the passages so we write",
    "start": 1024.559,
    "duration": 5.581
  },
  {
    "text": "another function generate answer this is",
    "start": 1027.14,
    "duration": 6.419
  },
  {
    "text": "going to take our the formatted query",
    "start": 1030.14,
    "duration": 4.5
  },
  { "text": "here", "start": 1033.559, "duration": 4.201 },
  {
    "text": "it's going to tokenize it using our bot",
    "start": 1034.64,
    "duration": 5.279
  },
  {
    "text": "tokenizer and then it's going to use a",
    "start": 1037.76,
    "duration": 6.72
  },
  {
    "text": "generator to generate a a prediction or",
    "start": 1039.919,
    "duration": 9.721
  },
  {
    "text": "generating answer okay so from there we",
    "start": 1044.48,
    "duration": 8.88
  },
  {
    "text": "that will output a load of token IDs",
    "start": 1049.64,
    "duration": 6.419
  },
  {
    "text": "which we obviously can't read so then we",
    "start": 1053.36,
    "duration": 5.46
  },
  {
    "text": "use this batch decode or the tokenizer",
    "start": 1056.059,
    "duration": 5.521
  },
  {
    "text": "decode to decode them into human",
    "start": 1058.82,
    "duration": 6.12
  },
  { "text": "readable text", "start": 1061.58, "duration": 6.12 },
  {
    "text": "like that so if we then go ahead and",
    "start": 1064.94,
    "duration": 5.58
  },
  {
    "text": "actually run that we will see that we",
    "start": 1067.7,
    "duration": 5.339
  },
  {
    "text": "want to focus on this bit here the first",
    "start": 1070.52,
    "duration": 6.24
  },
  {
    "text": "electric power system was built in 1881",
    "start": 1073.039,
    "duration": 7.321
  },
  {
    "text": "at gadaming in England I was powered by",
    "start": 1076.76,
    "duration": 6.84
  },
  {
    "text": "two oils and then and there so if we",
    "start": 1080.36,
    "duration": 6.96
  },
  {
    "text": "look at that answer or what we looked at",
    "start": 1083.6,
    "duration": 8.12
  },
  {
    "text": "here we can see that it is basically",
    "start": 1087.32,
    "duration": 6.719
  },
  {
    "text": "reformulating that interface in there",
    "start": 1091.72,
    "duration": 5.56
  },
  {
    "text": "into a more concise answer so we see in",
    "start": 1094.039,
    "duration": 6.901
  },
  {
    "text": "1881 of gold arming in England and so on",
    "start": 1097.28,
    "duration": 8.34
  },
  {
    "text": "so that's pretty cool now what if we go",
    "start": 1100.94,
    "duration": 6.239
  },
  {
    "text": "a little further if we ask some more",
    "start": 1105.62,
    "duration": 4.26
  },
  {
    "text": "questions you say how was the first",
    "start": 1107.179,
    "duration": 4.74
  },
  {
    "text": "Wireless message sent and this time",
    "start": 1109.88,
    "duration": 4.44
  },
  {
    "text": "we're going to return five of these",
    "start": 1111.919,
    "duration": 4.38
  },
  {
    "text": "contacts so we're going to return more",
    "start": 1114.32,
    "duration": 6.0
  },
  {
    "text": "information and ideally this should give",
    "start": 1116.299,
    "duration": 7.201
  },
  {
    "text": "us give the BART generation model more",
    "start": 1120.32,
    "duration": 5.28
  },
  {
    "text": "information to produce an answer from so",
    "start": 1123.5,
    "duration": 4.679
  },
  {
    "text": "it should generally speaking be able to",
    "start": 1125.6,
    "duration": 4.5
  },
  {
    "text": "produce a better answer if we give it",
    "start": 1128.179,
    "duration": 3.961
  },
  {
    "text": "more of that information but not all the",
    "start": 1130.1,
    "duration": 4.74
  },
  {
    "text": "time in this case we say we see first",
    "start": 1132.14,
    "duration": 6.18
  },
  {
    "text": "Wireless meshes sent in 1866 so on and",
    "start": 1134.84,
    "duration": 5.699
  },
  { "text": "so on okay", "start": 1138.32, "duration": 5.16 },
  {
    "text": "nice short answer which is good we set",
    "start": 1140.539,
    "duration": 5.161
  },
  {
    "text": "that by setting the max length up here",
    "start": 1143.48,
    "duration": 5.4
  },
  {
    "text": "at 14. and you know I don't know the",
    "start": 1145.7,
    "duration": 4.68
  },
  {
    "text": "answer to this question so what we can",
    "start": 1148.88,
    "duration": 4.26
  },
  {
    "text": "do is you know not just rely on the",
    "start": 1150.38,
    "duration": 4.74
  },
  {
    "text": "model to actually give us the answer",
    "start": 1153.14,
    "duration": 4.44
  },
  {
    "text": "which is a problem that we see a lot",
    "start": 1155.12,
    "duration": 6.66
  },
  {
    "text": "with the gbt 3 chat gbt and so on models",
    "start": 1157.58,
    "duration": 6.599
  },
  {
    "text": "we can actually have a look at what",
    "start": 1161.78,
    "duration": 4.2
  },
  {
    "text": "where this information is actually",
    "start": 1164.179,
    "duration": 3.0
  },
  { "text": "coming from", "start": 1165.98, "duration": 3.86 },
  { "text": "so", "start": 1167.179, "duration": 2.661 },
  {
    "text": "we can see here I think this is probably",
    "start": 1170.78,
    "duration": 6.68
  },
  { "text": "the most relevant part", "start": 1174.32, "duration": 3.14 },
  { "text": "so this guy", "start": 1177.5, "duration": 3.24 },
  {
    "text": "claimed to have transmitted an",
    "start": 1179.24,
    "duration": 3.24
  },
  {
    "text": "electrical signal through the atmosphere",
    "start": 1180.74,
    "duration": 4.679
  },
  { "text": "at this point right", "start": 1182.48, "duration": 5.46 },
  {
    "text": "and I don't think AMD other contexts",
    "start": 1185.419,
    "duration": 4.801
  },
  {
    "text": "rarely give us any more information on",
    "start": 1187.94,
    "duration": 4.2
  },
  {
    "text": "there so we can see that according to",
    "start": 1190.22,
    "duration": 4.02
  },
  {
    "text": "this context and if we wanted we could",
    "start": 1192.14,
    "duration": 4.02
  },
  {
    "text": "provide a link back to where that was",
    "start": 1194.24,
    "duration": 5.04
  },
  {
    "text": "actually from that does at least seem to",
    "start": 1196.16,
    "duration": 6.6
  },
  {
    "text": "be true now this is probably a good",
    "start": 1199.28,
    "duration": 6.0
  },
  {
    "text": "example of when this is useful so if we",
    "start": 1202.76,
    "duration": 4.56
  },
  {
    "text": "ask a question like where did covid-19",
    "start": 1205.28,
    "duration": 5.7
  },
  {
    "text": "originate and we get this like random",
    "start": 1207.32,
    "duration": 6.84
  },
  {
    "text": "answer and I think most of us probably",
    "start": 1210.98,
    "duration": 5.1
  },
  {
    "text": "know that this isn't this is kind of",
    "start": 1214.16,
    "duration": 5.34
  },
  {
    "text": "nonsense right so it's a zoonotic",
    "start": 1216.08,
    "duration": 5.94
  },
  {
    "text": "disease it's transmitted from one animal",
    "start": 1219.5,
    "duration": 5.22
  },
  {
    "text": "to another okay let's have a look at",
    "start": 1222.02,
    "duration": 5.82
  },
  {
    "text": "where this is coming from and we can see",
    "start": 1224.72,
    "duration": 5.88
  },
  {
    "text": "that all of these contacts don't",
    "start": 1227.84,
    "duration": 5.9
  },
  {
    "text": "actually contain anything about covid-19",
    "start": 1230.6,
    "duration": 6.9
  },
  {
    "text": "and so we can pretty confident in saying",
    "start": 1233.74,
    "duration": 5.799
  },
  {
    "text": "that this is nonsense and simply the",
    "start": 1237.5,
    "duration": 5.4
  },
  {
    "text": "reason is that this model has never seen",
    "start": 1239.539,
    "duration": 5.041
  },
  {
    "text": "anything about covid-19 the BART",
    "start": 1242.9,
    "duration": 3.54
  },
  {
    "text": "generation model it hasn't seen anything",
    "start": 1244.58,
    "duration": 3.479
  },
  {
    "text": "about that because the training data it",
    "start": 1246.44,
    "duration": 4.2
  },
  {
    "text": "was trained on was from before that time",
    "start": 1248.059,
    "duration": 6.301
  },
  {
    "text": "and as well none of the contexts that we",
    "start": 1250.64,
    "duration": 6.0
  },
  {
    "text": "have indexed here contain anything about",
    "start": 1254.36,
    "duration": 4.679
  },
  {
    "text": "it either so it can be pretty useful to",
    "start": 1256.64,
    "duration": 4.68
  },
  {
    "text": "include that particularly when it comes",
    "start": 1259.039,
    "duration": 5.281
  },
  {
    "text": "to fact checking things like that and",
    "start": 1261.32,
    "duration": 4.56
  },
  {
    "text": "then let's finish your final few",
    "start": 1264.32,
    "duration": 3.78
  },
  {
    "text": "questions was Warren current I'm not",
    "start": 1265.88,
    "duration": 5.1
  },
  {
    "text": "going to check these uh but I'm pretty",
    "start": 1268.1,
    "duration": 5.64
  },
  { "text": "sure so this one is true", "start": 1270.98, "duration": 5.52 },
  {
    "text": "first person on the Moon Neil Armstrong",
    "start": 1273.74,
    "duration": 5.7
  },
  {
    "text": "we I think all know that is true and",
    "start": 1276.5,
    "duration": 6.72
  },
  {
    "text": "what is NASA's most expensive project I",
    "start": 1279.44,
    "duration": 6.96
  },
  {
    "text": "think this one is possibly possibly true",
    "start": 1283.22,
    "duration": 6.12
  },
  {
    "text": "possibly not I can't remember but",
    "start": 1286.4,
    "duration": 5.94
  },
  {
    "text": "nonetheless we we get some pretty cool",
    "start": 1289.34,
    "duration": 6.3
  },
  {
    "text": "answers there so that's it for this",
    "start": 1292.34,
    "duration": 5.94
  },
  {
    "text": "video in this example walkthrough of",
    "start": 1295.64,
    "duration": 4.74
  },
  {
    "text": "abstractive or generative question",
    "start": 1298.28,
    "duration": 4.86
  },
  {
    "text": "answering I hope this has been useful",
    "start": 1300.38,
    "duration": 5.4
  },
  {
    "text": "and interesting so thank you very much",
    "start": 1303.14,
    "duration": 4.5
  },
  {
    "text": "for watching and I will see you again in",
    "start": 1305.78,
    "duration": 4.879
  },
  { "text": "the next one bye", "start": 1307.64, "duration": 3.019 }
]
