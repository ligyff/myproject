from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from langchain.agents import load_tools, initialize_agent, AgentType, agent
from langchain.chains import llm

import os

from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

os.environ["OPENAI_API_KEY"] = ''


def buy_xlb(days: int):
    return "成功"


def buy_jz(input: str):
    return "成功"


def sue_for_peace(addend: str):
    value=addend.split(",")


    a=int(value[0]) + int(value[1])
    return a


@require_http_methods(["GET"])
def chat01(request):
    xlb = Tool.from_function(func=buy_xlb,
                             name="buy_xlb",
                             description="当你需要买一份小笼包时候可以使用这个工具,他的输入为帮我买一份小笼包,他的返回值为是否成功"
                             )
    jz = Tool.from_function(func=buy_jz,
                            name="buy_jz",
                            description="当你需要买一份饺子时候可以使用这个工具,他的输入为帮我买一份饺子,他的返回值为是否成功"
                            )

    sfp = Tool.from_function(func=sue_for_peace,
                                     name="sue_for_peace",
                                     description="求两个数字的和"
                                     )
    tools = [sfp]

    llm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0)

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    # 运行 agent
    c = agent.run("100+234+12+111+11+111+111+111等于")


    return JsonResponse({"a": c})
