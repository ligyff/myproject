from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from langchain.agents import load_tools, initialize_agent, AgentType, agent
from langchain.chains import llm

import os

from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool, tool
from pydantic import BaseModel, Field


class emailinfo(BaseModel):
    to: str = Field(description="邮件接受人")
    title: str = Field(description="标题")
    body: str = Field(description="邮件体")


def sendemail(to: str, title: str, body: str):
    print(to)
    print(title)
    print(body)

    return "发送成功"


@require_http_methods(["GET"])
def chat02(request):
    send = Tool.from_function(func=sendemail,
                              name="sendemail",
                              description="发送邮件。方法中有3个参数",
                              args_schema=emailinfo)
    tools = [send]

    llm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0.8)

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    # 运行 agent
    c = agent.run("给test@gmail.com发送入职邮件通知在12月1日入职")

    return JsonResponse({"a": c})
