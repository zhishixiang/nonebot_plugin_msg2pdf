from nonebot import get_driver,on_command,on_message
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me, keyword
from nonebot.adapters import Event
from .config import Config

__plugin_meta = PluginMetadata(
    name="msg2pdf",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)

async def is_forward_msg(event:Event) -> bool:
    """
    检测消息类型是否为合并转发且是否为私聊
    > 参数：
        - event: MessageEvent 对象

    > 返回值：
        - 是合并转发消息：True
        - 不是合并转发消息：False
    """
    print(event.get_type)
    return True

weather = on_command("天气", rule=is_forward_msg, aliases={"weather", "查天气"}, priority=10, block=True)
help = on_message(rule=keyword("help","帮助","怎么","说明","教程"), priority=10, block=True)

@weather.handle()
async def weather_handler():
    await weather.finish("114514")

# 发送帮助信息
@help.handle()
async def help_handler():
    await help.finish({
        "欢迎使用消息转发bot，只需向我发送合并转发消息，我就能将消息另存为pdf，快来试试吧"
    })
