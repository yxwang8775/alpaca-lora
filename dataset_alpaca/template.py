squad = ['context:{context}',
         'An entity in context is {answer}',
         '{answer} is the answer of the following question:']

e = {"instruction": "",
     "input": "",
     "output": ""},

PATTERNS = {
    "rte": {
        0: [{"instruction": "Based on the paragraph provided, write a sentence that we can inferred from it.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Based on the given paragraph, write a sentence that we can know from it.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Write a sentence that is definitely correct based the the given context.",
             "input": "Context: {sentence1}",
             "output": "{sentence2}"}
            ],
        1: [{
                "instruction": "Based on the paragraph provided, write a related sentence that we cannot inferred from the paragraph.",
                "input": "{sentence1}",
                "output": "{sentence2}"},
            {"instruction": "Based on the given paragraph, write a sentence that we cannot know from it.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Write a sentence that is definitely wrong based on the the given context.",
             "input": "Context: {sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Write a sentence that conflicts with the the given context.",
             "input": "Context: {sentence1}",
             "output": "{sentence2}"},
            ],
    },
    "mnli": {
        0: [{"instruction": "Based on the sentence provided, write a sentence that we can inferred from it.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Based on the given paragraph provided, write a sentence that we can know from it.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Write a sentence that is definitely correct based on the the given context.",
             "input": "Context: {premise}",
             "output": "{hypothesis}"},
            ],
        1: [{"instruction": "Write a sentence that is related to the given one.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            ],
        2: [{"instruction": "Based on the sentence provided, write a related sentence that we cannot inferred from it.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Based on the given paragraph provided, write a sentence that we cannot know from it",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Write a sentence that is definitely wrong based on the the given context",
             "input": "Context: {premise}",
             "output": "{hypothesis}"},
            {"instruction": "Write a sentence that conflicts with the the given context",
             "input": "Context: {premise}",
             "output": "{hypothesis}"},
            ],
    },
    "qnli": {
        0: [
            {"instruction": "Based on the given paragraph, generate a question whose answer is in the paragraph.",
             "input": "{sentence}",
             "output": "{question}"},
            {"instruction": "Based on the information provided, generate a question about it.",
             "input": "{sentence}",
             "output": "{question}"},
        ],
        1: [
            {"instruction": "Based on the given paragraph, generate a question whose answer is not in the paragraph.",
             "input": "{sentence}",
             "output": "{question}"},
            {
                "instruction": "Based on the information provided, generate a question about it but we cannot know the answer from the information.",
                "input": "{sentence}",
                "output": "{question}"},
        ]
    },
    "wnli": {
        0: [{"instruction": "Based on the paragraph provided, write a sentence that we can inferred from it.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Based on the given paragraph, write a sentence that we can know from it.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Write a sentence that is definitely correct based the the given context.",
             "input": "Context: {sentence1}",
             "output": "{sentence2}"}
            ],
        1: [{
            "instruction": "Based on the paragraph provided, write a related sentence that we cannot inferred from the paragraph.",
            "input": "{sentence1}",
            "output": "{sentence2}"},
            {"instruction": "Based on the given paragraph, write a sentence that we cannot know from it.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Write a sentence that is definitely wrong based on the the given context.",
             "input": "Context: {sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Write a sentence that conflicts with the the given context.",
             "input": "Context: {sentence1}",
             "output": "{sentence2}"},
        ],
    },
    "snli": {
        0: [{"instruction": "Based on the sentence provided, write a sentence that we can inferred from it.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Based on the given paragraph provided, write a sentence that we can know from it.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Write a sentence that is definitely correct based on the the given context.",
             "input": "Context: {premise}",
             "output": "{hypothesis}"},
            ],
        1: [{"instruction": "Write a sentence that is related to the given one.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            ],
        2: [{"instruction": "Based on the sentence provided, write a related sentence that we cannot inferred from it.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Based on the given paragraph provided, write a sentence that we cannot know from it",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Write a sentence that is definitely wrong based on the the given context",
             "input": "Context: {premise}",
             "output": "{hypothesis}"},
            {"instruction": "Write a sentence that conflicts with the the given context",
             "input": "Context: {premise}",
             "output": "{hypothesis}"},
            ],
    },
    "wic": {0: [
        {"instruction": "The following sentence contains the word '{word}', write another sentence"
                        " that also contains '{word}' and the word '{word}'has the same meaning.",
         "input": "{sentence1}",
         "output": "{sentence2}"},
        {"instruction": "Given a sentence containing the word '{word}', write another sentence"
                        " containing the word 'word', and the word mean the same thing.",
         "input": "{sentence1}",
         "output": "{sentence2}"},
    ],
        1: [
            {"instruction": "The following sentence contains the word '{word}', write another sentence"
                            " that also contains '{word}' and the word '{word}'has the same meaning.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Given a sentence containing the word '{word}', write another sentence"
                            " containing the word 'word', and the word mean the same thing.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
        ],
    },
    "sst2": {
        0: [
            {"instruction": "Write a movie review in positive sentiment.",
             "input": "",
             "output": "{text}"},
        ],
        1: [
            {"instruction": "Write a movie review in positive sentiment.",
             "input": "",
             "output": "{text}"},
        ],
        # 0: [("The critic think negatively of the movie.\nShort movie review: ",
        #      "{sentence}"),
        #     ("The movie is seen negatively based on the following review.\nReview: ",
        #      "{sentence}"),
        #     ("The following review have a negative opinion of the movie.\nReview: ",
        #      "{sentence}"),
        #     ("Write a negative movie review.\nMovie review: ",
        #      "{sentence}"),
        #     ("Generate a short movie review that has negative sentiment.\nMovie review: ",
        #      "{sentence}")],
        # 1: [("The critic think positively of the movie.\nShort movie review: ",
        #      "{sentence}"),
        #     ("The movie is seen positively based on the following review.\nReview: ",
        #      "{sentence}"),
        #     ("The following review have a positive opinion of the movie.\nReview: ",
        #      "{sentence}"),
        #     ("Write a positive movie review.\nMovie review: ",
        #      "{sentence}"),
        #     ("Generate a short movie review that has positive sentiment.\nMovie review: ",
        #      "{sentence}")]
    },
    "aeslc": [
        # ("What is the subject line for this email?\n\n{body}\n\nSubject Line:",
        #  "{subject}"),
        # ("Write a subject line for this message:\n\n{body}\n\nSubject Line:",
        #  "{subject}"),
        # ("{body}\nWrite a subject line for this email.", "{subject}"),
        # ("Here is an email: {body}\nWhat is a potential subject line for this "
        #  "email?", "{subject}"),
        # ("{body}\nPropose a subject line for this email?", "{subject}"),
        # ("This is the content of an email: {body}\nWhat was the subject line "
        #  "for this email?", "{subject}"),
        # ("This is an email\n{body}\n\nWhat is the subject of this email?",
        #  "{subject}"),
        {"instruction": "Generate a subject line for this email.",
         "input": "{email_body}",
         "output": "{subject_line}"},
        {"instruction": "Write an email with the following subject.",
         "input": "Subject:{subject_line}\n\nEmail:",
         "output": "{email_body}"},
        {"instruction": "Write an email with the subject line.",
         "input": "{subject_line}\n\n",
         "output": "{email_body}"},

    ],
    "cnn_dailymail": [
        {"instruction": "Write an article according to the highlights.",
         "input": "Highlights: {highlights}.\n\nArticle: ",
         "output": "{article}"},
        {"instruction": "Write an article using the following points.",
         "input": "{highlights}\n\nArticle: ",
         "output": "{article}"},
        {"instruction": "Write an article based on the highlights provided.",
         "input": "{highlights}",
         "output": "{article}"},

    ],
    "gigaword": [
        {"instruction": "Write a text based on the summary.",
         "input": "Summary: {summary}.\n\nText: ",
         "output": "{document}"},
    ],

    "trec": {
        0: [
            {"instruction": "Ask me a question that can be answered with an entity.",
             "input": "",
             "output": "{text}"},
        ],
        1: [
            {"instruction": "Ask me a question that can be answered with an abbreviation.",
             "input": "",
             "output": "{text}"},
        ],
        2: [
            {"instruction": "Ask me a question that can be answered with a description.",
             "input": "",
             "output": "{text}"},
        ],
        3: [
            {"instruction": "Ask me a question that can be answered with a human.",
             "input": "",
             "output": "{text}"},
        ],
        4: [
            {"instruction": "Ask me a question that can be answered with a location.",
             "input": "",
             "output": "{text}"},
        ],
        5: [
            {"instruction": "Ask me a question that can be answered with a numeric.",
             "input": "",
             "output": "{text}"},
        ],
    },
    "multi_news": [
        {"instruction": "Write an article based on the summary.",
             "input": "Summary:{summary}\n\nArticle:",
             "output": "{document}"},
        {"instruction": "Expand the given summary to an article.",
             "input": "Summary:{summary}\n\nArticle:",
             "output": "{document}"},
    ],
    "samsum": [
        {"instruction": "Write a dialog about anything you want.",
             "input": "",
             "output": "{dialogue}"},
        {"instruction": "Write a dialog based on the given summary.",
             "input": "Summary:{summary}\n\nDialog:",
             "output": "{dialogue}"},

    ],
    "xsum": [

        {"instruction": "Write an article based on the summary.",
         "input": "Summary:{summary}\n\nArticle:",
         "output": "{document}"},
        {"instruction": "Expand the given summary to an article.",
         "input": "Summary:{summary}\n\nArticle:",
         "output": "{document}"},
    ],
    "squad": [
        {"instruction": "Write a question about the given context.",
         "input": "Context:{context}\n\nQuestion:",
         "output": "{question}"},
        {"instruction": "Given a context and a question about it. Answer the question.",
         "input": "Context:{context}\n\nQuestion:{question}\n\nAnswer:",
         "output": "{answer}"},
        {"instruction": "Based on the given article, answer the following question.",
         "input": "Article:{context}\n\nQuestion:{question}\n\nThe answer is:",
         "output": "{answer}"},
        {"instruction": "Write a question that you can find the answer in the given article:",
         "input": "Article:{context}\n\nQuestion:",
         "output": "{question}"},
    ],

    "drop": [  # pre

        {"instruction": "Write a question about the given context.",
         "input": "Context:{context}\n\nQuestion:",
         "output": "{question}"},
        {"instruction": "Given a context and a question about it. Answer the question.",
         "input": "Context:{context}\n\nQuestion:{question}\n\nAnswer:",
         "output": "{answer}"},
        {"instruction": "Based on the given article, answer the following question.",
         "input": "Article:{context}\n\nQuestion:{question}\n\nThe answer is:",
         "output": "{answer}"},
        {"instruction": "Write a question that you can find the answer in the given article:",
         "input": "Article:{context}\n\nQuestion:",
         "output": "{question}"},

        # # ("Answer based on context:\n\n{context}\n\n{question}", "{answer}"),
        # ("{context}\n\nAnswer this question based on the article: {question}",
        #  "{answer}"),
        # # ("{context}\n\n{question}", "{answer}"),
        # ("{context}\nAnswer this question: {question}", "{answer}"),
        # ("{context}\n\nBased on the above article, answer the following question. "
        #  "{question}", "{answer}"),
        # ("Context: {context}\n\nQuestion: {question}\n\nAnswer:", "{answer}"),
        # ("Write an article that answers the following question: {question}",
        #  "{context}"),
        # # ("Write a question about the following article: {context}\n\nQuestion "
        # #  "about the article:", "{question}"),
        # ("Write a question about the following article: {context}\n\nQuestion "
        #  "about the article: {question}\n\n The answer is:", "{answer}"),
        # ("{context}\n\nAsk a question about this article.{question} The answer is ", "{answer}"),
    ],

    "cosmos_qa": [  # pre
        {"instruction": "Write a question about the given context.",
         "input": "Context:{context}\n\nQuestion:",
         "output": "{question}"},
        {"instruction": "Given a context and a question about it. Answer the question.",
         "input": "Context:{context}\n\nQuestion:{question}\n\nAnswer:",
         "output": "{answer}"},
        {"instruction": "Based on the given article, answer the following question.",
         "input": "Article:{context}\n\nQuestion:{question}\n\nThe answer is:",
         "output": "{answer}"},
        {"instruction": "Write a question that you can find the answer in the given article:",
         "input": "Article:{context}\n\nQuestion:",
         "output": "{question}"},
    ],
    "ag_news": {
        0: [
            {"instruction": "Write an article about world.",
             "input": "",
             "output": "{text}"},
        ],
        1: [
            {"instruction": "Write an article about sports.",
             "input": "",
             "output": "{text}"},
        ],
        2: [
            {"instruction": "Write an article about business.",
             "input": "",
             "output": "{text}"},
        ],
        3: [
            {"instruction": "Write an article about science and technology.",
             "input": "",
             "output": "{text}"},
        ],
        # 0: [("Write an article about world.", "{text}")],
        # 1: [("Write an article about sports.", "{text}")],
        # 2: [("Write an article about business.", "{text}")],
        # 3: [("Write an article about science and technology.", "{text}")],
    },
    # "bool_q": [
    #     ("{text}\n\nSee options at the end. Can we conclude that "
    #      "{question}?\n\n{options_}", "{answer}"),
    #     ("{text}\n\nMulti-choice problem: Is it true that "
    #      "{question}?\n\n{options_}\nThe answer is:", "{answer}"),
    #     ("{text}\n\n{question}?\n\n{options_}", "{answer}"),
    #     ("Text: {text}\n\nQuestion: {question}?\n\n{options_}", "{answer}"),
    #     ("{text}\n\nWhat's the best answer to this question: "
    #      "{question}?\n\n{options_}...A:", "{answer}"),
    #     ("{text}\nBased on the above text, what's the best answer to this "
    #      "question: {question}?\n\n{options_}", "{answer}"),
    #     ("{text}\nAnswer this question, making sure that the answer is "
    #      "supported by the text: {question}?\n\n{options_}", "{answer}"),
    #     ("{text}\n\nChoose your answer: Is the following statement correct "
    #      "based on the text\n\n{question}\n\n{options_}", "{answer}"),
    #     ("{title}\n\n{text}\n\n{options_}\nIs this statement correct "
    #      "\"{question}\"?", "{answer}"),
    #     ("Is it true that {question} based on the following "
    #      "text?\n\n{text}\n\n{options_}", "{answer}"),
    # ],
    "definite_pronoun_resolution": [  # pre


        {"instruction": "Write a sentence including the word \"{pronoun}\" that refers to {answer}.",
             "input": "",
             "output": "{sentence}"},
        {"instruction": "Write a sentence where the word \"{pronoun}\" refers to {answer}.",
             "input": "",
             "output": "{sentence}"},
    ],
    "mrpc": {
        0: [
            {"instruction": "Given a sentence, write another sentence that have the same meaning with it.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Write two sentences that have the same meaning.",
             "input": "",
             "output": "Sentence 1:{sentence1}\nSentence 2:{sentence2}"},
        ],
        1: [
            {"instruction": "Given a sentence, write another sentence that have different meaning from it.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Write two sentences that have different meanings.",
             "input": "",
             "output": "Sentence 1:{sentence1}\nSentence 2:{sentence2}"},
        ],
    },
    "qqp": {
        0: [
            {"instruction": "Given a question, write another question that is similar and asks different thing from it.",
             "input": "{question1}",
             "output": "{question2}"},
            {"instruction": "Write two questions that inquire about different information.",
             "input": "",
             "output": "First question: {question1}\nSecond question:{question2}"},
            {"instruction": "Write two questions that ask about different things.",
             "input": "",
             "output": "First question: {question1}\nSecond question:{question2}"},
        ],
        1: [
            {"instruction": "Given a question, write another question that asks the same thing with it.",
             "input": "{question1}",
             "output": "{question2}"},
            {"instruction": "Write two questions that inquire about the same information.",
             "input": "",
             "output": "First question: {question1}\nSecond question:{question2}"},
            {"instruction": "Write two questions that ask about the same thing.",
             "input": "",
             "output": "First question: {question1}\nSecond question:{question2}"}
        ]
    },
    "imdb": {
        0: [
            {"instruction": "Generate a short movie review that has negative sentiment.",
             "input": "",
             "output": "{text}"},

            {"instruction": "Write a short movie review that has a negative opinion of the movie.",
             "input": "",
             "output": "{text}"},

            {"instruction": "I don't like the movie. Write a short movie review.",
             "input": "",
             "output": "{text}"},

            ],
        1: [
            {"instruction": "Generate a short movie review that has positive sentiment.",
             "input": "",
             "output": "{text}"},

            {"instruction": "Write a short movie review that has a positive opinion of the movie.",
             "input": "",
             "output": "{text}"},

            {"instruction": "I like the movie. Write a short movie review.",
             "input": "",
             "output": "{text}"},
        ]
    },
    "paws": {
        0: [
            {"instruction": "Given a sentence, write another sentence that have the same meaning with it.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Write two sentences that have the same meaning.",
             "input": "",
             "output": "Sentence 1:{sentence1}\nSentence 2:{sentence2}"},
        ],
        1: [
            {"instruction": "Given a sentence, write another sentence that have different meaning from it.",
             "input": "{sentence1}",
             "output": "{sentence2}"},
            {"instruction": "Write two sentences that have different meanings.",
             "input": "",
             "output": "Sentence 1:{sentence1}\nSentence 2:{sentence2}"},
        ],
        # 0: [
        #     ("{sentence1}\nThis sentence has the same meaning as the following.\n",
        #      "{sentence2}\""),
        #     ("Here are the two sentences that have the same meaning.\n Sentence1:{sentence1}\nSentence2:",
        #      "{sentence2}\""),
        # ],
        # 1: [
        #     ("{sentence1}\nThis sentence does not have the same meaning as the following.\n",
        #      "{sentence2}\""),
        #     ("Here are the two sentences that have different meanings.\n Sentence1:{sentence1}\nSentence2:",
        #      "{sentence2}\""),
        # ],
    },

    "yelp_polarity": {
        0: [
            {"instruction": "Generate a short movie review that has negative sentiment.",
             "input": "",
             "output": "{text}"},

            {"instruction": "Write a short movie review that has a negative opinion of the movie.",
             "input": "",
             "output": "{text}"},

            {"instruction": "I don't like the movie. Write a short movie review.",
             "input": "",
             "output": "{text}"},

        ],
        1: [
            {"instruction": "Generate a short movie review that has positive sentiment.",
             "input": "",
             "output": "{text}"},

            {"instruction": "Write a short movie review that has a positive opinion of the movie.",
             "input": "",
             "output": "{text}"},

            {"instruction": "I like the movie. Write a short movie review.",
             "input": "",
             "output": "{text}"},
        ],
        # 0: [("The critic think negatively of the movie.\nShort movie review: ",
        #      "{sentence}"),
        #     ("The movie is seen negatively based on the following review.\nReview: ",
        #      "{sentence}"),
        #     ("The following review have a negative opinion of the movie.\nReview: ",
        #      "{sentence}"),
        #     ("Write a negative movie review.\nMovie review: ",
        #      "{sentence}"),
        #     ("Generate a short movie review that has negative sentiment.\nMovie review: ",
        #      "{sentence}")],
        # 1: [("The critic think positively of the movie.\nShort movie review: ",
        #      "{sentence}"),
        #     ("The movie is seen positively based on the following review.\nReview: ",
        #      "{sentence}"),
        #     ("The following review have a positive opinion of the movie.\nReview: ",
        #      "{sentence}"),
        #     ("Write a positive movie review.\nMovie review: ",
        #      "{sentence}"),
        #     ("Generate a short movie review that has positive sentiment.\nMovie review: ",
        #      "{sentence}")]
    },
    "ai2_arc": [
        # ("{question}\n\n{options_}", "{answer}"),
        # ("Question: {question}\n{options_}\nAnswer:", "{answer}"),
        # ("Question: {question}\n\nWhat is the correct answer to the question "
        #  "from the following choices?\n{options_}", "{answer}"),
        # ("Q: {question}\nWhat is the correct answer to this "
        #  "question?\n{options_}...A:", "{answer}"),
        # ("Choose your answer?\n\n{question}\n\n{options_}", "{answer}"),
        # ("Answer the question\n\n{question}\n{options_}", "{answer}"),
        # ("{question}\n\nPick the answer from these options\n\n{options_}",
        #  "{answer}"),
        {"instruction": "Write a question you would see in a school textbook.",
             "input": "",
             "output": "{question}"},
        {"instruction": "What's an example of a grad-school level question?",
         "input": "",
         "output": "{question}"},
        {"instruction": "I just took a test in school today. What question was I asked?",
         "input": "",
         "output": "{question}"},
    ],
    "anli": {
        0: [{"instruction": "Based on the sentence provided, write a sentence that we can inferred from it.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Based on the given paragraph provided, write a sentence that we can know from it.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Write a sentence that is definitely correct based on the the given context.",
             "input": "Context: {premise}",
             "output": "{hypothesis}"},
            ],
        1: [{"instruction": "Write a sentence that is related to the given one.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            ],
        2: [{"instruction": "Based on the sentence provided, write a related sentence that we cannot inferred from it.",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Based on the given paragraph provided, write a sentence that we cannot know from it",
             "input": "{premise}",
             "output": "{hypothesis}"},
            {"instruction": "Write a sentence that is definitely wrong based on the the given context",
             "input": "Context: {premise}",
             "output": "{hypothesis}"},
            {"instruction": "Write a sentence that conflicts with the the given context",
             "input": "Context: {premise}",
             "output": "{hypothesis}"},
            ],
    },
    # "coqa": [
    #     ("{text}\n\nAnswer the following "
    #      "questions:\n{numbered_questions}\n\nNumbered answers:",
    #      "{numbered_answers}"),
    #     ("Read the text and answer the "
    #      "questions.\n\n{text}\n\n{numbered_questions}\n\nNumbered answers:",
    #      "{numbered_answers}"),
    #     ("Answer the questions at the end based on the "
    #      "text.\n\n{text}\n\n{numbered_questions}\n\nNumbered answers:",
    #      "{numbered_answers}"),
    #     ("{text}\n\nAnswer this series of "
    #      "questions:\n\n{numbered_questions}\n\nNumbered answers:",
    #      "{numbered_answers}"),
    #     ("{text}\n\nWhat are the answers to this following set of "
    #      "questions:\n\n{numbered_questions}\n\nNumbered answers:",
    #      "{numbered_answers}"),
    #     ("{text}\n\nNow, provide a numbered list of answers to these "
    #      "questions:\n\n{numbered_questions}\n\nNumbered answers:",
    #      "{numbered_answers}"),
    #     ("{text}\n\n{numbered_questions}\n\nNumbered answers:",
    #      "{numbered_answers}"),
    #     ("{text}\n\n{numbered_questions}\n\nProvide a numbered list of "
    #      "answers.", "{numbered_answers}"),
    #     ("Make use of the article to answer the "
    #      "questions.\n\n{text}\n\n{numbered_questions}\n\nNumbered answers:",
    #      "{numbered_answers}"),
    #     ("{text}\n\nBased on the article and the following list of answers, "
    #      "write a list of questions.\n\n{numbered_answers}\n\nNumbered "
    #      "questions:", "{numbered_questions}"),
    # ],
    # "opinion_abstracts_rotten_tomatoes": [
    #     ("{numbered_reviews}\n\nWrite a one sentence summary of the reviews "
    #      "above.", "{critic_consensus}"),
    #     ("{numbered_reviews}\n\nWhat is a brief summary of "
    #      "the following reviews?", "{critic_consensus}"),
    #     ("{numbered_reviews}\nBased on these individual reviews, what is the "
    #      "critic consensus?", "{critic_consensus}"),
    #     ("{numbered_reviews}\nWhat is the consensus?", "{critic_consensus}"),
    #     ("Here are some reviews for a movie: {numbered_reviews}\n\nWhat was "
    #      "the overall consensus about the movie?", "{critic_consensus}"),
    #     ("Summarize the following movie "
    #      "reviews:\n\n{numbered_reviews}\n\nSummary:", "{critic_consensus}"),
    #     ("Write a one sentence review of the movie \"{movie}\".",
    #      "{critic_consensus}"),
    #     ("Write an ordered list of reviews about \"{movie}\".",
    #      "{numbered_reviews}"),
    #     ("The critic consesnsus is: {critic_consensus}. What reviews supported"
    #      " this critic consensus?", "{numbered_reviews}"),
    #     ("Which movie is the following review "
    #      "about?\n\n{first_review}\n\nMovie:", "{movie}"),
    # ],
    "common_gen": [
        {"instruction": "What are the keywords in the given sentence?",
             "input": "{target}",
             "output": "{concepts}"},
        {"instruction": "What are the most important words in the given sentence?",
             "input": "{target}",
             "output": "{concepts}"},
        {"instruction": "Identify the most salient words in this sentence.",
             "input": "{target}",
             "output": "{concepts}"},
        {"instruction": "Generate a sentence, and then tell me the concepts included in that sentence.",
             "input": "",
             "output": "Sentence:\n{target}\n\nConcepts:\n{concepts}"},

    ],
    # "dart": [
    #     ("Triple: {tripleset}\n\nWhat is a sentence that describes this triple?",
    #      "{target}"),
    #     ("Data: {tripleset}\n\nWhat would a sentence about this data be like?",
    #      "{target}"),
    #     ("Generate an approximately fifteen-word sentence that describes all "
    #      "this data: {tripleset}\n\n", "{target}"),
    #     ("Here is some data: {tripleset}.\n\nWrite a sentence that describes "
    #      "this data:", "{target}"),
    #     ("This is some data: {tripleset}.\n\nGenerate a detailed description "
    #      "of this data.", "{target}"),
    #     ("Generate a sentence about this data: {tripleset}\nSentence:",
    #      "{target}"),
    #     ("Write a sentence that about [{tripleset}].", "{target}"),
    #     ("Produce a long descriptive sentence that uses all these words: "
    #      "{tripleset}", "{target}"),
    #     ("What concepts are described in the following "
    #      "sentence?\n\n\"{target}\"\n\nReturn the answer as pairs of triples.",
    #      "{tripleset_newline}"),
    #     ("Create a set of triples that describes the content in the following "
    #      "sentence.\n\n{target}\n\n", "{tripleset_newline}"),
    # ],
    # "e2e_nlg": [
    #     ("Attributes: {meaning_representation}. Produce a detailed sentence "
    #      "about this restaurant.", "{target}"),
    #     ("Data: {meaning_representation}. Can you generate a sentence about "
    #      "this data?", "{target}"),
    #     ("Data: {meaning_representation}. What is a sentence that describe "
    #      "this data?", "{target}"),
    #     ("Here are some keywords about a "
    #      "restaurant:\n\n{meaning_representation}. Write a sentence that "
    #      "describes the following attributes of a restaurant.", "{target}"),
    #     ("Here is some data about a restaurant: {meaning_representation}. "
    #      "Write a sentence that includes the above data about a restaurant",
    #      "{target}"),
    #     ("Sentence: {meaning_representation}\n\nCan you represent the content "
    #      "in this sentence in data form?", "{target}"),
    #     ("Write a sentence about a restaurant with all the following "
    #      "attributes: {meaning_representation}\nSentence:", "{target}"),
    #     ("Write a sentence that is about a restaurant with all the following "
    #      "properties: {meaning_representation}\nSentence:", "{target}"),
    #     ("Produce a detailed sentence about a restaurant using the following "
    #      "words: {meaning_representation}\nSentence:", "{target}"),
    #     ("Generate a descriptive sentence about a restaurant using the "
    #      "following words:\n\n{meaning_representation}\nSentence:", "{target}"),
    # ],
    # "web_nlg_en": [
    #     ("{input_string}\n\nWhat is sentence that verbalizes this data?",
    #      "{target}"),
    #     ("Data: {input_string}\n\nSentence about the following data: ",
    #      "{target}"),
    #     ("Here is some data: {input_string}.\n\nWrite a sentence that "
    #      "describes this data.\nSentence:", "{target}"),
    #     ("This is some data: {input_string}.\n\nGenerate a detailed "
    #      "description of this data.\nSentence:", "{target}"),
    #     ("Generate a sentence about this data: {input_string}.\nSentence:",
    #      "{target}"),
    #     ("Generate a sentence that describes the following data: "
    #      "{input_string}.\nSentence:", "{target}"),
    #     ("Produce a long descriptive sentence that uses all these words: "
    #      "{input_string}.\nSentence:", "{target}"),
    #     ("Generate an approximately fifteen-word sentence that describes all "
    #      "this data: {input_string}.\nSentence:", "{target}"),
    #     ("Sentence: {target}\n\nWhat data can be extracted from this sentence?",
    #      "{input_string}"),
    #     ("Sentence: {target}\n\nWhat structured data could we extract from "
    #      "this sentence?", "{input_string}"),
    # ],
    "wiki_lingua_english_en": [
        ("Write an article based on this summary:\n\n{target}\n\nArticle:",
         "{source}"),
        ("Write an article based on this \"{target}\"\n\nArticle:", "{source}"),
    ],
    # "multirc": [
    #     ("{paragraph}\n\nQuestion: \"{question}\"\n\nResponse: "
    #      "\"{response}\"\n{options_}\nDoes the response correctly answer the "
    #      "question?\n\n", "{answer}"),
    #     ("{paragraph}\n\nQuestion: \"{question}\"\n\nResponse: "
    #      "\"{response}\"\n\nBased on the paragraph, is the response to the "
    #      "question is factually correct?\n\n{options_}", "{answer}"),
    #     ("{paragraph}\n\nQuestion: \"{question}\"\n\nAnswer: "
    #      "\"{response}\"\n\nIs this answer correct?\n\n{options_}...I think "
    #      "the answer is", "{answer}"),
    #     ("Paragraph: {paragraph}\n\nQuestion: \"{question}\"\n\nAnswer: "
    #      "\"{response}\"\n\nBased on the paragraph, choose if the answer is "
    #      "correct:\n\n{options_}", "{answer}"),
    #     ("{paragraph}\n\nChoose from options: Based on the paragraph, does the"
    #      " response \"{response}\" correctly answer the question "
    #      "\"{question}\"?\n\n{options_}", "{answer}"),
    #     ("{paragraph}\n\nChoose your answer: According to the above paragraph,"
    #      " the correct answer to the question \"{question}\" is "
    #      "\"{response}\"?\n\n{options_}", "{answer}"),
    #     ("{paragraph}\n\nAfter reading the above, is \"{response}\" the "
    #      "correct answer to the question \"{question}\"?\n\n{options_}",
    #      "{answer}"),
    #     ("{paragraph}\n\nQuestion: \"{question}\"\n\nAnswer: "
    #      "\"{response}\"\n\nIs this answer to the question correct?"
    #      "\n{options_}", "{answer}"),
    #     ("{paragraph}\nDo you have any questions?", "{question}"),
    #     ("{paragraph}\nWhat question would one ask from this paragraph?",
    #      "{question}"),
    # ],
    # stjokerli/TextToText_cb
    "cb": [
        ("{premise}\n\nBased on the paragraph above can we conclude that "
         "\"{hypothesis}\"?\n\n{options_}", "{answer}"),
        ("{premise}\n\nBased on that paragraph can we conclude that this "
         "sentence is true?\n{hypothesis}\n\n{options_}", "{answer}"),
        ("{premise}\n\nCan we draw the following conclusion (choose your "
         "answer)?\n{hypothesis}\n\n{options_}", "{answer}"),
        ("{premise}\nSelect from options. Does this next sentence follow, "
         "given the preceding text?\n{hypothesis}\n\n{options_}", "{answer}"),
        ("{premise}\nMulti-choice question: Can we infer the "
         "following?\n{hypothesis}\n\n{options_}", "{answer}"),
        ("Multi-choice problem: Read the following paragraph and determine if "
         "the hypothesis is true:\n\n{premise}\n\nHypothesis: "
         "{hypothesis}\n{options_}", "{answer}"),
        ("You will be given options, read the text and determine if the "
         "sentence is true:\n\n{premise}\n\nSentence: "
         "{hypothesis}\n{options_}", "{answer}"),
        ("Can we draw the following hypothesis from the context? "
         "\n\nContext:\n\n{premise}\n\nHypothesis: {hypothesis}\n{options_}",
         "{answer}"),
        ("Determine if the sentence is true based on the text "
         "below:\n{hypothesis}\n{options_}\n{premise}\n", "{answer}"),
        ("Generate a context and a hypothesis.",
         "Context: {premise}\n\nHypothesis: {hypothesis}"),
    ],
    "cola": [
        ("Sentence: \"{sentence}\"\nPick from options: would a linguist rate "
         "this sentence to be acceptable linguistically?\n\n{options_}...I "
         "think the answer is", "{answer}"),
        ("{sentence}\n\nHow would you consider the linguistic integrity of the"
         " preceding sentence?\n{options_}", "{answer}"),
        ("Test sentence: \"{sentence}\"\nIs this test sentence a correct "
         "grammatical English sentence?\n\n{options_}", "{answer}"),
        ("Sentence: \"{sentence}\"\nWould a linguist rate this sentence to be "
         "acceptable linguistically?\n\n{options_}", "{answer}"),
        ("Choose from options, is the following sentence linguistically "
         "acceptable?\n{sentence}\n{options_}", "{answer}"),
        ("Choose from the possible answers, would the following sentence, by "
         "the strictest standards, be considered correct by a "
         "linguist?\n\n{sentence}\n{options_}", "{answer}"),
        ("Multi-choice problem: Is the next sentence syntactically and "
         "semantically acceptable?\n\n{sentence}\n{options_}", "{answer}"),
        ("Would a linguist find the following sentence to be a valid English "
         "sentence grammatically?\n\n{sentence}\n{options_}", "{answer}"),
        ("Generate short a sentence that can be linguistically classified as "
         "{answer} ({options_})", "{sentence}"),
        ("Produce a brief English sentence that would be considered "
         "grammatically as category: {answer}\nAll categories: {options_}",
         "{sentence}"),
    ],

    "stsb": [
        ("{sentence1}\n{sentence2}\n\nRate the textual similarity of these two"
         " sentences on a scale from 0 to 5, where 0 is \"no meaning overlap\""
         " and 5 is \"means the same thing\".\n\n{options_}", "{answer}"),
        ("{sentence1}\n{sentence2}\n\nOn a scale from 0 to 5, where 0 is \"no "
         "meaning overlap\" and 5 is \"means the same thing\", how closely "
         "does the first sentence resemble the second one?\n\n{options_}",
         "{answer}"),
        ("Sentence 1: {sentence1}\n\n Sentence 2: {sentence2}\n\nFrom 0 to 5 "
         "(0=\"no meaning overlap\" and 5=\"means the same thing\"), how "
         "similar are the two sentences?\n\n{options_}", "{answer}"),
        ("Select from options: How similar are the following two "
         "sentences?\n\n{sentence1}\n{sentence2}\n\nGive the answer on a scale"
         " from 0 - 5, where 0 is \"not similar at all\" and 5 is \"means the "
         "same thing\".\n\n{options_}", "{answer}"),
        ("Single/multi-select question: Do the following sentences say the "
         "same thing?\n\n{sentence1}\n{sentence2}\n\nReturn your answer on a "
         "scale from 0 to 5, where 0 is \"not similar\" and 5 is \"very "
         "similar\".\n\n{options_}", "{answer}"),
        ("Rate the similarity of the following two sentences on a scale from 0"
         " to 5, where 0 is \"no meaning overlap\" and 5 is \"means the same "
         "thing\"?\n\n{sentence1}\n{sentence2}\n\n{options_}", "{answer}"),
        ("On a scale from 0-5, where 0 is \"not similar\" and 5 is \"very "
         "similar\", how similar is the sentence \"{sentence1}\" to the "
         "sentence \"{sentence2}\"?\n\n{options_}", "{answer}"),
        ("How similar are these two sentences, on a scale from 0-5 (0 is \"not"
         " similar\" and 5 is \"very "
         "similar\")?\n\n{sentence1}\n{sentence2}\n\n{options_}", "{answer}"),
        ("{sentence1}\n\nGenerate a new sentence that is, on a scale from 0 to"
         " 5, a {answer} in textual similarity to the above sentence.",
         "{sentence2}"),
        ("{sentence2}\n\nWhat is a sentence that would be (on a scale from 0 "
         "to 5) a {answer} out of 5 in terms of textual similarity to the "
         "above sentence?", "{sentence1}"),
    ],
    "hellaswag": [
        ("What happens next in this paragraph?\n\n{context}\n{options_}",
         "{answer}"),
        ("Multi-choice problem: Continue writing the next sentence in this "
         "paragraph:\n\n{context}\n\n{options_}", "{answer}"),
        ("Select from options: Continue writing the next "
         "sentence.\n\n{context}\n\n{options_}\nAnswer:", "{answer}"),
        ("This is a test of commonsense with single/multi-choices. Complete "
         "the next sentence:\n\n{context}\n\n{options_}\nThe answer is:",
         "{answer}"),
        ("Write the next sentence in this paragraph:\n\n{context}\n\n{options_}",
         "{answer}"),
        ("Multi-select problem: How does the next paragraph "
         "end?\n\n{context}\n\n{options_}", "{answer}"),
        ("{options_}Choose from options above and answer: What most naturally "
         "follows?\n\n{context}\nAnswer:", "{answer}"),
        ("What happens next?\n\n{context}\n\n{options_}", "{answer}"),
        ("What is the most logical next event?\n\n{context}\n\n{options_}",
         "{answer}"),
        ("Write the next sentence in the following "
         "story.\n\n{context}\n\n{options_}. The answer should be", "{answer}"),
    ],
    "piqa": [
        ("Here is a goal: {goal}\n\nHow would you accomplish this "
         "goal?\n\n{options_}", "{answer}"),
        ("Here is a goal: {goal}\n\nWhich way makes more sense to accomplish "
         "this goal?\n\n{options_}", "{answer}"),
        ("This is a question with answer options. Goal: {goal}\n\nWhich of the"
         " following methods is more reasonable for accomplishing this "
         "goal?\n\n{options_}...I think the answer is", "{answer}"),
        ("Objective: {goal}\n\nWhich of the following solutions is more sound "
         "in terms of naive physics reasoning?\n\n{options_}", "{answer}"),
        ("Multi-choice problem: Choose from the options at the end, and answer"
         " how do you do this: {goal}\n\n{options_}", "{answer}"),
        ("What is the best way to: {goal}\n\n{options_}\nAnswer:", "{answer}"),
        ("Single/multi-choice problem: Which of the following solutions is "
         "better for the following goal:\n{goal}\n\n{options_}", "{answer}"),
        ("This question has options. How would someone go about accomplishing "
         "this goal?\n{goal}\n\n{options_}", "{answer}"),
        ("What's an example of a task that requires knowledge of physical "
         "objects to perform?", "{goal}"),
        ("What kind of task would test someone's ability to perform physical "
         "reasoning?", "{goal}"),
    ],
    "openbookqa": [
        ("{fact}\n{question}\n\n{options_}", "{answer}"),
        ("This question has options. Select from options: Read this fact: "
         "\"{fact}\"\n\nNow answer this question: \"{question}\"\n\n{options_}",
         "{answer}"),
        ("Given the fact \"{fact}\", what is the answer to the question or "
         "completion \"{question}\"\n\n{options_}", "{answer}"),
        ("Multi-select: Knowing that \"{fact}\", how would one answer "
         "\"{question}\"\n\n{options_}...A:", "{answer}"),
        ("Use evidence from the fact that {fact} to answer the following "
         "question. Choose from options. \"{question}\"\n\n{options_}",
         "{answer}"),
        ("Fact: {fact}\nQuestion: {question}\n\nWhat's the answer? {options_}",
         "{answer}"),
        ("Use this fact to answer the question: {fact}\n\n{question}\n\n"
         "{options_}\n\nThe answer is:", "{answer}"),
        ("What sentence would provide a factual answer to this question: "
         "\"{question}\"", "{fact}"),
        ("What is a random fact?", "{fact}"),
        ("Generate a sentence that contains a fact.", "{fact}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "lambada": [
        ("{sentence}", "{answer}"),
        ("Complete the following text: {sentence}", "{answer}"),
        ("\"{sentence} _ ...\" What is the word in the blank space (_)? The "
         "answer is", "{answer}"),
        ("You will be given a text below. Complete the text.\n{sentence}",
         "{answer}"),
        ("TEXT: {sentence}", "{answer}"),
        ("SENTENCE: {sentence}", "{answer}"),
        ("Complete: {sentence}", "{answer}"),
        ("Text complete: {sentence}", "{answer}"),
        ("Complete text: {sentence}", "{answer}"),
        ("Continue writing the following text: {sentence}", "{answer}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "cot_gsm8k": [
        ("{question} Let's think first. Chain of thought:",
         "{chain_of_thought}\nTherefore, the answer is {answer}."),
        ("{question} Think carefully first, then make a decision:",
         "{chain_of_thought} So, the answer is {answer}."),
        ("{question} Let's be accurate as possible.",
         "{chain_of_thought}\nThe answer: {answer}."),
        ("{question} Give me reasons, before answering the question",
         "{chain_of_thought} So the final answer is {answer}."),
        ("Lizzy: {question}.\nMe: Hmmm, let me think. I think this is the "
         "detailed solution:", "{chain_of_thought} Final answer: {answer}."),
        ("Question: {question} Think carefully first, then make a decision:",
         "{chain_of_thought} So the answer is {answer}."),
        ("Give the step-by-step reasoning process and then the final answer. "
         "{question}", "{chain_of_thought}\nThe final answer: {answer}."),
        ("{question}\nThoughts? Step-by-step reasoning:",
         "{chain_of_thought}\nThus, the answer is {answer}."),
        ("My question is: {question} Your thoughts:",
         "{chain_of_thought} The final answer: {answer}."),
        ("{question} Let's answer step by step:",
         "{chain_of_thought} The answer: {answer}."),
    ],
    # Not in FLAN Templates (flan_templates):
    "cot_strategyqa": [
        ("{question}\nThink slowly and carefully, before giving your answer.",
         "{chain_of_thought}\nSo, the answer is {answer}."),
        ("{question} Please answer step by step:",
         "{chain_of_thought}\nSo, the final answer is {answer}."),
        ("{question}\nChain of thought:",
         "{chain_of_thought} The answer is {answer}."),
        ("Answer the following question by reasoning step-by-step. {question}",
         "{chain_of_thought} Therefore, the final answer is {answer}."),
        ("{question} Given the above question, please answer with reasoning "
         "first!", "{chain_of_thought}\nTherefore, the answer is {answer}."),
        ("{question} Think carefully first, then make a decision:",
         "{chain_of_thought} So, the answer is {answer}."),
        ("Q: {question} Now, let's think step by step:",
         "{chain_of_thought}\nThe answer: {answer}."),
        ("Answer the following question, but give the rationale first. "
         "{question}", "{chain_of_thought} So the final answer is {answer}."),
        ("{question} Hmmm, my chain of thoughts:",
         "{chain_of_thought} Final answer: {answer}."),
        ("Let's answer this question slowly: {question}\n",
         "{chain_of_thought} So the answer is {answer}."),
    ],
    # Not in FLAN Templates (flan_templates):
    "cot_creak": [
        ("Given the following question, let's solve step-by-step. {question}\n",
         "{chain_of_thought}\nThe final answer: {answer}."),
        ("My question: {question}\nPlease think gradually:",
         "{chain_of_thought}\nThus, the answer is {answer}."),
        ("Give the rationale and then the answer. {question}",
         "{chain_of_thought} The final answer: {answer}."),
        ("Q: {question}\nChain-of-thought:",
         "{chain_of_thought} The answer: {answer}."),
        ("{question}\nChain of thought and solution for this question is:",
         "{chain_of_thought}\nSo, the answer is {answer}."),
        ("Question: {question} Let's think first. Step-by-step reasoning:",
         "{chain_of_thought}\nSo, the final answer is {answer}."),
        ("{question}\nYour chain-of-thought:",
         "{chain_of_thought} The answer is {answer}."),
        ("{question} Step-by-step reasoning process:",
         "{chain_of_thought} Therefore, the final answer is {answer}."),
        ("{question} The thought process:",
         "{chain_of_thought}\nTherefore, the answer is {answer}."),
        ("{question} Let's think first. Step-by-step reasoning process:",
         "{chain_of_thought} So, the answer is {answer}."),
    ],
    # Not in FLAN Templates (flan_templates):
    "cot_qasc": [
        ("Question: {question}\nLet's be accurate as possible and think "
         "step-by-step.", "{chain_of_thought}\nThe answer: {answer}."),
        ("{question} Let's solve this problem gradually.\n",
         "{chain_of_thought} So the final answer is {answer}."),
        ("Question to you: {question}.\nLet's reason step-by-step:",
         "{chain_of_thought} Final answer: {answer}."),
        ("{question} Think carefully first, then make a decision. My thoughts:",
         "{chain_of_thought} So the answer is {answer}."),
        ("{question} Let's be accurate as possible.",
         "{chain_of_thought}\nThe final answer: {answer}."),
        ("Q: {question}\nLet's think step by step below.\n",
         "{chain_of_thought}\nThus, the answer is {answer}."),
        ("Let's think step by step! {question}\nThe thinking starts now:",
         "{chain_of_thought} The final answer: {answer}."),
        ("{question}\nHmmm, let me think. I don't want to be wrong, so I got "
         "to be careful.", "{chain_of_thought} The answer: {answer}."),
        ("Use reasoning to answer the following question. {question}",
         "{chain_of_thought}\nSo, the answer is {answer}."),
        ("{question} OK. Let's think hard:",
         "{chain_of_thought}\nSo, the final answer is {answer}."),
    ],
    # Not in FLAN Templates (flan_templates):
    "cot_esnli": [
        ("{question}\nLet's solve step-by-step:",
         "{chain_of_thought} The answer is {answer}."),
        ("{question} Step by step answer:",
         "{chain_of_thought} Therefore, the final answer is {answer}."),
        ("{question} Stream of thoughts:",
         "{chain_of_thought}\nTherefore, the answer is {answer}."),
        ("{question} Now, let's be accurate as possible. Some thinking first:",
         "{chain_of_thought} So, the answer is {answer}."),
        ("Denny asked: {question}.\nLe: OK, so how can I answer with some "
         "explanation?\n", "{chain_of_thought}\nThe answer: {answer}."),
        ("Student: {question}.\nTeacher: Let's think:\n",
         "{chain_of_thought} So the final answer is {answer}."),
        ("{question} Let's be accurate as possible and think first.",
         "{chain_of_thought} Final answer: {answer}."),
        ("Please answer the following question by reasoning step-by-step. "
         "{question}. Step-by-step reasoning:",
         "{chain_of_thought} So the answer is {answer}."),
        ("{question} A step-by-step solution is:\n",
         "{chain_of_thought}\nThe final answer: {answer}."),
        ("Leo: {question}\nMei: OK, So, let's think first...\nMe:",
         "{chain_of_thought}\nThus, the answer is {answer}."),
    ],
    # Not in FLAN Templates (flan_templates):
    "cot_ecqa": [
        ("{question}\nPlease answer and provide answer explanation.",
         "{chain_of_thought} The final answer: {answer}."),
        ("{question}\nStep-by-step reasoning process below:\n",
         "{chain_of_thought} The answer: {answer}."),
        ("{question} Hmmm, let me think.",
         "{chain_of_thought}\nSo, the answer is {answer}."),
        ("{question}\nLet's think now! Step-by-step reasoning:",
         "{chain_of_thought}\nSo, the final answer is {answer}."),
        ("next question: {question}\nreasoning:",
         "{chain_of_thought} The answer is {answer}."),
        ("Use reasoning to lead to the answer of the following question:\n"
         "{question}\n Reasoning process:",
         "{chain_of_thought} Therefore, the final answer is {answer}."),
        ("{question} Let's give stream of consciousness first:",
         "{chain_of_thought}\nTherefore, the answer is {answer}."),
        ("{question} Let's think step by step:",
         "{chain_of_thought} So, the answer is {answer}."),
        ("I'll give you a question, please answer with step-by-step reasoning "
         "process. {question}\n", "{chain_of_thought}\nThe answer: {answer}."),
        ("{question}\nLet's think carefully first. Step-by-step reasoning "
         "process:", "{chain_of_thought} So the final answer is {answer}."),
    ],
    # Not in FLAN Templates (flan_templates):
    "cot_sensemaking": [
        ("{question} Let's reason step by step:",
         "{chain_of_thought} Final answer: {answer}."),
        ("Question: {question}\nPlease answer this question gradually:",
         "{chain_of_thought} So the answer is {answer}."),
        ("See question below:\n{question}\nReason slowly and give your answer.",
         "{chain_of_thought}\nThe final answer: {answer}."),
        ("OK. You'll be given the following question. Please do "
         "chain-of-thought reasoning.\n{question}",
         "{chain_of_thought}\nThus, the answer is {answer}."),
        ("{question} Let's be accurate as possible. So think first.",
         "{chain_of_thought}\nThe final answer: {answer}."),
        ("Q: {question}\nLet's solve this gradually.\n",
         "{chain_of_thought} The answer is {answer}."),
        ("Let's think step by step! {question}\n",
         "{chain_of_thought} The answer: {answer}."),
        ("{question}\nHmmm, let me think. I want to lay out the solution "
         "in details.", "{chain_of_thought} The answer is {answer}."),
        ("Answer the following question, with explanation first. {question}",
         "{chain_of_thought}\nSo, the answer is {answer}."),
        ("{question} Let me think hard. Detailed solution:",
         "{chain_of_thought}\nThe answer is {answer}."),
    ],
    # Not in FLAN Templates (flan_templates):
    "stream_aqua": [
        ("Q: {question} Let's give some random thoughts before answering.",
         "{chain_of_thought}\nTherefore, the answer is {answer}."),
        ("{question} Hmmm, my stream of consciousness:",
         "{chain_of_thought} So, the answer is {answer}."),
        ("Give a quick stream of consciousness before answering the following "
         "question. {question}", "{chain_of_thought}\nThe answer: {answer}."),
        ("Use some thinking to answer the following question. {question}",
         "{chain_of_thought} So the final answer is {answer}."),
        ("Student: {question}.\nAnother student: Let's say, hmmm...\n",
         "{chain_of_thought} Final answer: {answer}."),
        ("{question} Think first, then make a decision. Some random thoughts:",
         "{chain_of_thought} So the answer is {answer}."),
        ("{question} Now, let's think a bit. Some random thoughts:",
         "{chain_of_thought}\nThe final answer: {answer}."),
        ("{question} Stream of consciousness:",
         "{chain_of_thought}\nThus, the answer is {answer}."),
        ("Question: {question} Random thoughts:",
         "{chain_of_thought} The final answer: {answer}."),
        ("{question} OK. Let's think. Some random thoughts first:",
         "{chain_of_thought} The answer: {answer}."),
        ("Give stream of consciousness and then the final answer. {question}",
         "{chain_of_thought}\nThe final answer: {answer}."),
        ("{question} Stream of consciousness first, then make a decision:",
         "{chain_of_thought}\nThus, the answer is {answer}."),
        ("Question: {question} Let's think first. Some random reasoning:",
         "{chain_of_thought} The final answer: {answer}."),
        ("Some question: {question}\nSome stream of consciousness:",
         "{chain_of_thought} The answer: {answer}."),
        ("{question} Let's think first. Stream of consciousness:",
         "{chain_of_thought}\nSo, the answer is {answer}."),
    ],
    # Not in FLAN Templates (flan_templates):
    "stream_qed": [
        ("{question}\nSteam of consciousness below:\n",
         "{chain_of_thought}\nSo, the answer is {answer}."),
        ("{question} Let's give stream of consciousness first:",
         "{chain_of_thought}\nSo, the final answer is {answer}."),
        ("Quoc: {question}\nHW Chung: OK, some thoughts:",
         "{chain_of_thought} The answer is {answer}."),
        ("Q: {question} Let's give stream of consciousness first:",
         "{chain_of_thought} Therefore, the final answer is {answer}."),
        ("I got a question for you: {question}\nLet's think first:",
         "{chain_of_thought}\nTherefore, the answer is {answer}."),
        ("{question} Okie... think carefully first, then make a decision:",
         "{chain_of_thought} So, the answer is {answer}."),
        ("Output a stream of consciousness before answering the following. "
         "{question}", "{chain_of_thought}\nThe answer: {answer}."),
        ("{question} Let's think fast. Stream of consciousness:",
         "{chain_of_thought} So the final answer is {answer}."),
        ("Use stream of consciousness to answer the following. {question}",
         "{chain_of_thought} Final answer: {answer}."),
        ("Q: {question}\nLet's give stream of consciousness below\n",
         "{chain_of_thought} So the answer is {answer}."),
        ("Give a stream of consciousness and then the final answer. {question}",
         "{chain_of_thought}\nSo, the final answer is {answer}."),
        ("{question} OK. Let's think. My stream of consciousness:",
         "{chain_of_thought} The answer is {answer}."),
        ("Answer the following Q with stream of consciousness. {question}",
         "{chain_of_thought} Therefore, the final answer is {answer}."),
        ("Give some stream of consciousness and then the answer. {question}",
         "{chain_of_thought}\nTherefore, the answer is {answer}."),
        ("{question} Let's have some stream of consciousness first.",
         "{chain_of_thought} So, the answer is {answer}."),
    ],
    # Not in FLAN Templates (flan_templates):
    "strategyqa": [
        ("Yes or no: {question}", "{answer}"),
        ("{question} Answer yes or no.", "{answer}"),
        ("Question: {question} Answer:", "{answer}"),
        ("Answer yes or no after the question mark: {question}", "{answer}"),
        ("Answer yes or no: {question}", "{answer}"),
        ("Reply yes or no: {question}", "{answer}"),
        ("{question} Yes or no:", "{answer}"),
        ("{question}\n\nIt's yes or no? The answer is", "{answer}"),
        ("Yes/no: {question}", "{answer}"),
        ("{question}. The answer:", "{answer}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "unified_qa_science_inst": [
        ("{question}\n{options_}", "{answer}"),
        ("{question}\n{options_}The answer is:", "{answer}"),
        ("{question} {options_}\nYour answer:", "{answer}"),
        ("{question}\n{options_}\n", "{answer}"),
        ("{question}\n-\n{options_}", "{answer}"),
        ("{question}\n{options_}\n", "{answer}"),
        ("{question} {options_}\n", "{answer}"),
        ("Answer this:\n{question}\n{options_}", "{answer}"),
        ("{question}\n\n{options_}\n\n", "{answer}"),
        ("Answer this question: {question}\n{options_}. Answer:", "{answer}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "bigbench:simple_arithmetic_json.gen.blueridge_vocab.0_shot.30_examples": [
        ("What is the value of {inputs}? Answer:", "{targets}"),
        ("What is the solution of the following "
         "problem?\n{inputs}\n\nSolution:", "{targets}"),
        ("Reply with the result of this math problem:\n\n{inputs}",
         "{targets}"),
        ("{inputs} The answer is", "{targets}"),
        ("Solve this math problem: {inputs}\n\n", "{targets}"),
        ("{inputs}\n\n", "{targets}"),
        ("{inputs} A:", "{targets}"),
        ("Q: {inputs} A:", "{targets}"),
        ("Question: {inputs}\nAnswer:", "{targets}"),
        ("Math problem: {inputs}\nAnswer:", "{targets}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "bigbench:auto_debugging.gen.blueridge_vocab.0_shot.34_examples": [
        ("Answer the following question:\n{inputs}", "{targets}"),
        ("Given the question below, answer directly after the question "
         "ended:\n{inputs}", "{targets}"),
        ("{inputs} I think the answer is:", "{targets}"),
        ("{inputs} The answer is", "{targets}"),
        ("{inputs} The answer of this coding problem is", "{targets}"),
        ("{inputs} Hmm... The answer is", "{targets}"),
        ("{inputs} Hmm... I believe the correct answer should be", "{targets}"),
        ("Answer the following coding question:\n\n{inputs}\n\n", "{targets}"),
        ("See this interesting question:\n{inputs}\nThe quick answer is:",
         "{targets}"),
        ("{inputs} A:", "{targets}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "bigbench:strategyqa.gen.blueridge_vocab.0_shot.1000_examples": [
        ("{inputs} First answer yes or no, then explain.", "{targets}"),
        ("Answer this question (yes or no) then explain why:\n{inputs}",
         "{targets}"),
        ("Yes or no: {inputs} The answer followed by explanation is:",
         "{targets}"),
        ("Answer yes or no after the question mark, then explain the reason: "
         "{inputs}", "{targets}"),
        ("Yes or no first, then explain the reason: {inputs}", "{targets}"),
        ("Yes/no: {inputs}", "{targets}"),
        ("You will be given a question. Answer yes or no first, then give the "
         "reason.\n{inputs}\n\n", "{targets}"),
        ("{inputs} Answer followed by reasoning:", "{targets}"),
        ("Answer + your thought for the following question: {inputs}\n",
         "{targets}"),
        ("{inputs} Answer + thought is:", "{targets}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "bigbench:sufficient_information.gen.blueridge_vocab.0_shot.39_examples": [
        ("{inputs}\n\n", "{targets}"),
        ("Answer this question or say \"I don't know\": {inputs}", "{targets}"),
        ("Q: {inputs} A:", "{targets}"),
        ("Answer the given question (if the question cannot be answered due to"
         " lack of information, answer \"I don't know\").\n{inputs}",
         "{targets}"),
        ("Question: {inputs}\n\nAnswer:", "{targets}"),
        ("Q: {inputs}\nA:", "{targets}"),
        ("The answer (if no enough information, say I don't know) to "
         "\"{inputs}\" is:", "{targets}"),
        ("Question that might not be answerable: {inputs}. Answer:",
         "{targets}"),
        ("Question: {inputs}\nAnswer:", "{targets}"),
        ("{inputs} A:", "{targets}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "predict_next_turn_dialog": [
        ("{dialog_}", "{answer}"),
        ("{dialog_}\n", "{answer}"),
        ("Read the dialog and predict the next turn. {dialog_}\n", "{answer}"),
        ("What is the next dialog turn? {dialog_}", "{answer}"),
        ("See the conversation. {dialog_}", "{answer}"),
        ("Write the response. {dialog_}", "{answer}"),
        ("Write the conversation response. {dialog_}", "{answer}"),
        ("Fill in the response. {dialog_}", "{answer}"),
        ("What was likely said next? {dialog_}", "{answer}"),
        ("What was the response? {dialog_}", "{answer}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "t0_question_answer": [
        # t0 comes pre-templatized/formatted and generation task varies
        # e.g. QA or question generation
        ("{question}\n", "{answer}"),
        ("{question}\nAnswer:", "{answer}"),
        ("{question}\nA:", "{answer}"),
        ("Q:{question}\nA:", "{answer}"),
        ("Question: {question}\nAnswer:", "{answer}"),
        ("Answer the following question: {question}\nAnswer:", "{answer}"),
        ("Given the question: {question}\nThe answer is:", "{answer}"),
        ("{question}\nThe answer to this question is:", "{answer}"),
        ("Please answer the following question: {question}\nA:", "{answer}"),
        ("Please answer the following question: {question}\nAnswer:",
         "{answer}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "t0_multiple_choice_separated_options": [
        ("{question}\n{options_}", "{answer}"),
        ("{question}\n{options_}\nAnswer:", "{answer}"),
        ("{question}\n\n{options_}\nAnswer:", "{answer}"),
        ("Q: {question}\n\n{options_}\nA:", "{answer}"),
        ("Answer the following question: {question}\n\n{options_}\nAnswer:",
         "{answer}"),
        ("{options_}\n\n{question}\nAnswer:", "{answer}"),
        ("{options_}\nQ: {question}\nA:", "{answer}"),
        ("{question}\n\n{options_}\nThe answer is:", "{answer}"),
        ("{options_}\nGiven those answer options, answer the "
         "question: {question}\nA:", "{answer}"),
        ("Q: {question}\n\n{options_}\nThe answer is:", "{answer}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "program_synthesis_dmcc_python": [
        ("{question}", "{answer}"),
        ("Write a program that answers the question. {question}\nAnswer:",
         "{answer}"),
        ("Write code that solves this problem. {question}\nAnswer:",
         "{answer}"),
        ("Write a program that solves this problem. {question}\nSolution:",
         "{answer}"),
        ("Solve this problem. {question}\nSolution:", "{answer}"),
        ("Solve this problem. {question}\nSolution in code:", "{answer}"),
        ("{question}\n\nCode solution:", "{answer}"),
        ("Coding Problem.\n{question}\n\nSolution:", "{answer}"),
        ("{question}\n\nCode solution in Python:", "{answer}"),
        ("[code]{question}[BEGIN]", "{answer}[DONE]"),
    ],
    # Not in FLAN Templates (flan_templates):
    "program_synthesis_dr_repair": [
        ("My broken code is below:\n{question}\nThe fixed code should be:",
         "{answer}"),
        ("My broken code is below:\n{question}\nThe fixed code:", "{answer}"),
        ("Incorrect code:\n{question}\nFixed code:", "{answer}"),
        ("Incorrect code:\n{question}\n\nThe correct version:", "{answer}"),
        ("This code is broken:\n{question}\n\nShow the fixed version:",
         "{answer}"),
        ("Broken:\n{question}\n\nFixed:", "{answer}"),
        ("Broken code:\n{question}\n\nFixed Code:", "{answer}"),
        ("The following code is not correct.\n{question}\n\nPropose solution "
         "code:", "{answer}"),
        ("The following code is not correct.\n{question}\n\nCome up with code "
         "that would fix this:", "{answer}"),
        ("Fix this code. ```{question}```\n\nA potential fix:```",
         "{answer}```"),
    ],
    # Not in FLAN Templates (flan_templates):
    "program_synthesis_dr_repair_error_comments": [
        ("My broken code is below with errors in comments:\n{question}\nThe "
         "fixed code should be:", "{answer}"),
        ("My broken code is below with errors in comments:\n{question}\nThe "
         "fixed code, with no more errors or error comments:", "{answer}"),
        ("Errors are described inline in comments. Incorrect "
         "code:\n{question}\nFixed code:", "{answer}"),
        ("See errors in comments. Incorrect code:\n{question}\n\nThe correct "
         "version:", "{answer}"),
        ("This code is broken:\n{question}\n\nVersion which fixes commented "
         "errors:", "{answer}"),
        ("Broken:\n```{question}```\n\nFixed:```", "{answer}```"),
        ("Broken code (see error comments):\n{question}\n\nFixed:", "{answer}"),
        ("Coding Challenge: fix the errors, as commented:\n{question}\n\nFixed:",
         "{answer}"),
        ("Challenge Question. See code:\n{question}\n\nA potential fix:",
         "{answer}"),
        ("Fix this code. ```{question}```\n\nA potential fix:```",
         "{answer}```"),
    ],
    # Not in FLAN Templates (flan_templates):
    "cot_stream_general_input_inversion": [
        # CoT + Answer --> Question
        ("Given the following reasoning and answer, what was the question? "
         "{chain_of_thought}\n The answer: {answer}", "The question {question}"
         ),
        # CoT + Answer --> Question
        ("For this chain-of-thought reasoning and answer, what was the "
         "question?\n{chain_of_thought}\n A: {answer}", "Q: {question}"),
        # Question + Answer --> CoT
        ("Consider the question. {question}\n What is the step-by-step "
         "reasoning process to arrive at the answer: {answer}?",
         "{chain_of_thought}"),
        # Question + Answer --> CoT
        ("Question. {question}\nAnswer. {answer}\nWhat step-by-step "
         "reasoning justifies that answer?", "Reasoning: {chain_of_thought}"),
        # Question + Answer --> CoT
        ("Q: {question}\nA: {answer}\nExplain how we arrive at this answer: ",
         "Explanation: {chain_of_thought}"),
        # CoT --> Question + Answer
        ("Given the rationale, provide a reasonable question and answer. "
         "Step-by-step reasoning process: {chain_of_thought}\n The question "
         "and answer:", "{question}\nThe answer is {answer}"),
        # CoT --> Question + Answer
        ("{chain_of_thought}\nThis justifies what answer for what question? Q "
         "& A: ", "{question}\n{answer}"),
        # CoT --> Question + Answer
        ("{chain_of_thought}is the reasoning for what question and answer pair?",
         "Q: {question}\nA: {answer}"),
        # Answer --> Question + CoT
        ("Come up with a question and reasoning that would justify this "
         "answer: {answer}", "The question is: {question}\n"
                             "Step-by-step reasoning process: {chain_of_thought}\n"),
        # Answer --> Question + CoT
        ("Creatively image a question and justification for this answer: "
         "{answer}", "The question is: {question}\nStep-by-step reasoning "
                     "process: {chain_of_thought}\n"),
        # CoT + Answer --> Question
        ("What was the question for this implicit rationale, and corresponding"
         " answer?\n{chain_of_thought}\n The answer: {answer}",
         "The question: {question}"),
        # Question + Answer --> CoT
        ("Consider the question. {question}\n If the answer is '{answer}'; "
         "explain the reasoning:", "{chain_of_thought}"),
        # Question + Answer --> CoT
        ("Explain simply why {answer} is the correct answer to: {question}. "
         "Explanation:", "{chain_of_thought}"),
        # CoT --> Question + Answer
        ("Given the stream of consciousness rationale, provide a reasonable "
         "question and answer. Rationale: {chain_of_thought}\n The question "
         "and answer:", "{question}\nThe answer is {answer}"),
        # CoT --> Question + Answer
        ("Stream of consciousness rationale: {chain_of_thought}\nThe question "
         "and answer pair are described below.", "Q: {question}\nA: {answer}"),
        # CoT --> Question + Answer
        ("Reconstruct a question, answer pair from this explanation: "
         "{chain_of_thought}\n", "Q:{question}\nA:{answer}"),
        # Answer --> Question + CoT
        ("Come up with a question and stream of consciousness reasoning that "
         "would justify this answer: {answer}", "The question is: {question}\n"
                                                "Stream of consciousness: {chain_of_thought}\n"),
        # Answer --> Question + CoT
        ("Imagine a question and stream-of-consciousness explanation for which"
         " this is the answer: {answer}", "Question: {question}\n"
                                          "Stream-of-consciousness: {chain_of_thought}"),
    ],
    # Not in FLAN Templates (flan_templates):
    "predict_next_turn_dialog_input_inversion": [
        ("Consider this response: {answer}\nWhat was the preceding dialog?",
         "{dialog_}"),
        ("{answer}\nThe preceding conversation:", "{dialog_}"),
        ("Read this response and predict the preceding dialog. {answer}\n",
         "{dialog_}"),
        ("What might have been said before this? {answer}", "{dialog_}"),
        ("{answer}\nPrevious conversation:", "{dialog_}"),
        ("What came before. {answer}", "{dialog_}"),
        ("Write the conversation that led to this response. {answer}",
         "{dialog_}"),
        ("See this dialog response. {answer} What came before?", "{dialog_}"),
        ("Imagine the conversation that came before this response? Response: "
         "{answer}", "{dialog_}"),
        ("If this is the response, what came before? Response {answer}",
         "{dialog_}"),
    ],

    # Not in FLAN Templates (flan_templates):
    # NB: ALL NatInstV2 tasks come somewhat pre-templatized.
    "natinst_v2": [
        ("{Definition}\n\n{input}", "{output}"),
        ("You will be given a definition of a task first, then some input of "
         "the task.\n{Definition}\n\n{input}\nOutput:", "{output}"),
        ("Definition: {Definition}\nInput: {input}\nOutput:", "{output}"),
        ("Instructions: {Definition}\nInput: {input}\nOutput:", "{output}"),
        ("{Definition}\nQ: {input}\nA: ", "{output}"),
        ("Given the task definition and input, reply with output. "
         "{Definition}\n\n{input}\n", "{output}"),
        ("Teacher:{Definition}\nTeacher: Now, understand the problem? Solve "
         "this instance: {input}\nStudent:", "{output}"),
        ("Q: {Definition}\n{input}\nA:", "{output}"),
        ("Detailed Instructions: {Definition}\nProblem:{input}\nSolution:",
         "{output}"),
        ("Detailed Instructions: {Definition}\nQ: {input}\nA:", "{output}"),
    ],
}


def get_pattern(task_name):
    pattern_mapping = {

    }
    if task_name not in pattern_mapping:
        raise PATTERNS[task_name]
    else:
        return PATTERNS[pattern_mapping[task_name]]


def get_label_field(task_name):
    label_field = {
        'sst2': 'label'
    }
    if task_name not in label_field:
        return 'label'
    else:
        return label_field[task_name]
