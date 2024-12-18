#!/usr/bin/env python
# coding: utf-8

# # Lesson 2: Datasets For Reinforcement Learning Training

# ### Loading and exploring the datasets
# 
# "Reinforcement Learning from Human Feedback" **(RLHF)** requires the following datasets:
# - Preference dataset
#   - Input prompt, candidate response 0, candidate response 1, choice (candidate 0 or 1)
# - Prompt dataset
#   - Input prompt only, no response

# #### Preference dataset

# In[1]:


preference_dataset_path = 'sample_preference.jsonl'


# In[2]:


import json


# In[3]:


preference_data = []


# In[4]:


with open(preference_dataset_path) as f:
    for line in f:
        preference_data.append(json.loads(line))


# - Print out to explore the preference dataset

# In[5]:


sample_1 = preference_data[0]


# In[6]:


print(type(sample_1))


# In[7]:


# This dictionary has four keys
print(sample_1.keys())


# - Key: 'input_test' is a prompt.

# In[8]:


sample_1['input_text']


# In[9]:


# Try with another examples from the list, and discover that all data end the same way
preference_data[2]['input_text'][-50:]


# - Print 'candidate_0' and 'candidate_1', these are the completions for the same prompt.

# In[10]:


print(f"candidate_0:\n{sample_1.get('candidate_0')}\n")
print(f"candidate_1:\n{sample_1.get('candidate_1')}\n")


# - Print 'choice', this is the human labeler's preference for the results completions (candidate_0 and candidate_1)

# In[11]:


print(f"choice: {sample_1.get('choice')}")


# #### Prompt dataset

# In[12]:


prompt_dataset_path = 'sample_prompt.jsonl'


# In[13]:


prompt_data = []


# In[14]:


with open(prompt_dataset_path) as f:
    for line in f:
        prompt_data.append(json.loads(line))


# In[15]:


# Check how many prompts there are in this dataset
len(prompt_data)


# **Note**: It is important that the prompts in both datasets, the preference and the prompt, come from the same distribution. 
# 
# For this lesson, all the prompts come from the same dataset of [Reddit posts](https://github.com/openai/summarize-from-feedback).

# In[16]:


# Function to print the information in the prompt dataset with a better visualization
def print_d(d):
    for key, val in d.items():        
        print(f"key:{key}\nval:{val}\n")


# In[17]:


print_d(prompt_data[0])


# In[18]:


# Try with another prompt from the list 
print_d(prompt_data[1])


# In[ ]:




