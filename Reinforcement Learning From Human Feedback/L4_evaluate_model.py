#!/usr/bin/env python
# coding: utf-8

# # Lesson 4: Evaluate the Tuned Model

# #### Project environment setup
# 
# - Install Tensorboard (if running locally)
# ```Python
# !pip install tensorboard
# ```

# ### Explore results with Tensorboard

# In[1]:


get_ipython().run_line_magic('load_ext', 'tensorboard')


# In[2]:


port = get_ipython().run_line_magic('env', 'PORT1')
get_ipython().run_line_magic('tensorboard', '--logdir reward-logs --port $port --bind_all')


# In[3]:


# Look at what this directory has
get_ipython().run_line_magic('ls', 'reward-logs')


# In[4]:


port = get_ipython().run_line_magic('env', 'PORT2')
get_ipython().run_line_magic('tensorboard', '--logdir reinforcer-logs --port $port --bind_all')


# In[5]:


port = get_ipython().run_line_magic('env', 'PORT3')
get_ipython().run_line_magic('tensorboard', '--logdir reinforcer-fulldata-logs --port $port --bind_all')


# - The dictionary of 'parameter_values' defined in the previous lesson

# In[6]:


parameter_values={
        "preference_dataset": \
    "gs://vertex-ai/generative-ai/rlhf/text_small/summarize_from_feedback_tfds/comparisons/train/*.jsonl",
        "prompt_dataset": \
    "gs://vertex-ai/generative-ai/rlhf/text_small/reddit_tfds/train/*.jsonl",
        "eval_dataset": \
    "gs://vertex-ai/generative-ai/rlhf/text_small/reddit_tfds/val/*.jsonl",
        "large_model_reference": "llama-2-7b",
        "reward_model_train_steps": 1410,
        "reinforcement_learning_train_steps": 320,
        "reward_model_learning_rate_multiplier": 1.0,
        "reinforcement_learning_rate_multiplier": 1.0,
        "kl_coeff": 0.1,
        "instruction":\
    "Summarize in less than 50 words"}


# **Note:** Here, we are using "text_small" for our datasets for learning purposes. However for the results that we're evaluating in this lesson, the team used the full dataset with the following hyperparameters:
# 
# ```Python
# parameter_values={
#         "preference_dataset": \
#     "gs://vertex-ai/generative-ai/rlhf/text/summarize_from_feedback_tfds/comparisons/train/*.jsonl",
#         "prompt_dataset": \
#     "gs://vertex-ai/generative-ai/rlhf/text/reddit_tfds/train/*.jsonl",
#         "eval_dataset": \
#     "gs://vertex-ai/generative-ai/rlhf/text/reddit_tfds/val/*.jsonl",
#         "large_model_reference": "llama-2-7b",
#         "reward_model_train_steps": 10000,
#         "reinforcement_learning_train_steps": 10000, 
#         "reward_model_learning_rate_multiplier": 1.0,
#         "reinforcement_learning_rate_multiplier": 0.2,
#         "kl_coeff": 0.1,
#         "instruction":\
#     "Summarize in less than 50 words"}
# ```

# ### Evaluate using the tuned and untuned model

# In[7]:


import json


# In[8]:


eval_tuned_path = 'eval_results_tuned.jsonl'


# In[9]:


eval_data_tuned = []


# In[10]:


with open(eval_tuned_path) as f:
    for line in f:
        eval_data_tuned.append(json.loads(line))


# In[11]:


# Import for printing purposes
from utils import print_d


# In[12]:


# Look at the result produced by the tuned model
print_d(eval_data_tuned[0])


# In[13]:


eval_untuned_path = 'eval_results_untuned.jsonl'


# In[14]:


eval_data_untuned = []


# In[15]:


with open(eval_untuned_path) as f:
    for line in f:
        eval_data_untuned.append(json.loads(line))


# In[16]:


# Look at the result produced by the untuned model
print_d(eval_data_untuned[0])


# ### Explore the results side by side in a dataframe

# In[17]:


# Extract all the prompts
prompts = [sample['inputs']['inputs_pretokenized']
           for sample in eval_data_tuned]


# In[18]:


# Completions from the untuned model
untuned_completions = [sample['prediction']
                       for sample in eval_data_untuned]


# In[19]:


# Completions from the tuned model
tuned_completions = [sample['prediction']
                     for sample in eval_data_tuned]


# - Now putting all together in one big dataframe

# In[20]:


import pandas as pd


# In[21]:


results = pd.DataFrame(
    data={'prompt': prompts,
          'base_model':untuned_completions,
          'tuned_model': tuned_completions})


# In[22]:


pd.set_option('display.max_colwidth', None)


# In[23]:


# Print the results
results

