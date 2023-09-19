from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage
)
from article import get_article
import validators

# prepare template for prompt
template = """You are an advanced AI assistant that summarizes online articles into bulleted lists.

Here's the article you need to summarize.

==================
{article_text}
==================

Now, provide a summarized version of the article in a bulleted list format.
"""

def summarize(article_url, model="gpt-3.5-turbo-16k"):
    # Validate Article URL
    valid = validators.url(article_url)
    if(not valid):
        return
     
    article = get_article(article_url)
    if(article and len(article) < 10):
        return "Please enter a News article URL"

    # format prompt
    prompt = template.format(article_text=article)
    
    # load the model
    chat = ChatOpenAI(model_name=model, temperature=0)

    # generate summary
    summary = chat([HumanMessage(content=prompt)])
    return summary.content