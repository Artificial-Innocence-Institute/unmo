from .unmo import Unmo
import sys

def _build_prompt(unmo):
    """AIインスタンスを取り、AIとResponderの名前を整形して返す"""
    return '{name}:{responder}> '.format(name=unmo.name,
                                         responder=unmo.responder_name)

def main():
    args = sys.argv

    print('Unmo System prototype : proto')
    proto = Unmo('proto')
    if (len(args) >= 2):
        f = open(args[1])
        line = f.readline() # 1行読み込む(改行文字も含まれる)
        while line:
            line = f.readline()
            proto.dialogue(line)
        f.close
    else:
        while True:
            text = input('> ')
            if not text:
                break

            response = proto.dialogue(text)
            print('{prompt}{response}'.format(prompt=_build_prompt(proto),
                                            response=response))
    proto.save()
