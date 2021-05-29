import gpt_2_simple as gpt2


def process(file_name, model_name):
    sess = gpt2.start_tf_sess()
    print("GPT-2 beginning fine-tuning using " + file_name + " as the corpus")
    gpt2.finetune(sess,
                  file_name,
                  model_name=model_name,
                  steps=1000)  # steps is max number of training steps

    single_text = gpt2.generate(sess, return_as_list=True)[0]
    return single_text
