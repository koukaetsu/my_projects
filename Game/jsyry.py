from sys import exit
import random
from textwrap import dedent



class System(object):
    clues = {
        '死者姓名：A同学。第5节课以上厕所为由出教室。': False,
        '保安室钥匙丢失？': False,
        'A同学和B同学在竞争保送名额。': False,
        '这场竞争最终以A同学的失败告终。A与B的关系不佳，B同学在1班。': False,
        'B同学在竞争中动用了关系？不正当竞争？': False,
        '1班第5课是体育课。': False,
        '上午第5节课原本是信息课，因为信息老师有事临时调成了语文。': False,
        '语文老师手机在第4节课下课后丢在2班没拿。': False
    }
    classin = False
    time_number = 12
    random_number = 0

    def list(self):
        clue_list = [key for key, value in self.clues.items() if value]
        return clue_list



class Engine(System):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene() #后面的current场景和此处的没啥关系了,这里只负责开场
        #print(f"目前的场景是{current_scene}")

        while True:

            next_scene_name = current_scene.enter() #调用返回的类的方法enter
            #print(f"下一个场景是{next_scene_name}") #返回到的值是激光武器库（举个例子，以此类推）
            # 此处current_scene将返回的类实例化了,例如：current_scene = LaserWeaponArmory()
            current_scene = self.scene_map.next_scene(next_scene_name) #current_scene = defscene
            #print(current_scene)



class Scene(System):

    def enter(self):
        print("该场景尚未配置")
        print("子类化它并实现enter()")
        exit(1)


class StartRoom(Scene):

    def enter(self):
        System.random_number += 1
        System.time_number = 12
        System.clues['死者姓名：A同学。第5节课以上厕所为由出教室。'] = True



        print(dedent("""
        你从梦中惊醒后发现已经毕业的自己居然坐在高中教室里，老师在讲台上讲着即使穿越99遍再听1遍也会听得睡着的课程。
        震惊起初充斥着你的大脑，然后你很快就接受了。
        也许这只是个梦境，还挺真的。你这么想着，掐了自己一下。
        好痛！
        熟悉到不能再熟悉得声音从讲台上传来“hello?”“有人吗？”
        哦，原来这节是语文课，而讲台上站着的正是你在高中最讨厌的老师。
        不对，这不是重点！
        重点是，为什么梦里会出现疼痛感？
        你开始有点慌了，从桌上的铅笔盒里拿出圆规扎了一下自己，
        啊！
        你痛得倒吸一口凉气。
        一切都似乎再告诉你，这并不是梦。
        我穿越了？你不可思议地瞪大了双眼。
        正回想着高中的点点滴滴，突然，窗外似乎有黑影坠了下去，你好奇地转过头，伴随着”咚“一声，你吓了一跳。
        有人坠楼？你心里出现了不太好的想法。
        这时，下课铃响了，逐渐有同学出了教室，然后就是一声尖叫。
        好吧，不好的想法真的发生了。
        你走出教室，看到3班的朋友着急地向你跑来，从她的口中得知，原来坠楼的是3班的A同学。
        据她所说，A同学在第5节课以上厕所为由出了教室，再次被发现就是刚刚坠楼之后了。
        A平时品学兼优，唯一的问题是比较沉默寡言（如果这也算问题？），这样的同学怎么会突然想不开呢？
        你皱起了眉头，联想到自己突然穿越到了高中的时候，心里突然产生一个奇怪的想法：
        “不会是让我阻止这场坠楼吧？”
        嗯……怎么不是呢？小说中不都这么写么？
        那么……
        这节是最后一节课，应该去食堂了。不过……真的要去吗？
        """))

        if System.random_number == 2:
            print(dedent("""
            等等，
            这段话是不是见过了？
            你被吓出了一声冷汗。
            好像似乎，你不仅仅是穿越，
            而是踏入了一个循环。
            """))

        #print(self.clue1)

        while True:
            action = input('>')

            if action == '不去':
                randomp = random.randint(0,1)

                if randomp == 0:
                    print(dedent("""
                    不，你怎么可能错过这种调查线索的好机会？
                    你趁着上厕所的功夫试图躲开排队，没想到今天不巧班主任点名。
                    他大喊着“人都来齐了再走”！
                    你叹了口气，站进了路队。
                    """))
                    return '食堂'

                elif randomp == 1:
                    print(dedent("""
                    不，你怎么可能错过这种调查线索的好机会？
                    你趁着上厕所的功夫试图躲开排队，运气不错，没有老师点名。
                    等同学们都走光了，你从厕所探出了头环顾四周。
                    哈哈，现在是我的主场啦！
                    """))
                    return '教学楼'

            elif action == '去':
                print(dedent("""
                有个道理是，人是铁，饭是钢。先吃饱肚子才能收集线索嘛。
                你赞同地点点头，跟着路队下了楼。
                """))
                return '食堂'

            elif action == '菜单':
                clue_list = super().list()
                print(f"当前已收集线索：{clue_list}")
                print(f"当前时间:{System.time_number}点")

            else:
                if System.random_number != 1:
                    print("不__去？")
                    print("等等，为什么这个字都崩坏了？！")
                else:
                    print("不去或去？")




class DiningRoom(Scene):


    def enter(self):

        print(f"当前时间:{System.time_number}点")
        if System.clues['保安室钥匙丢失？'] == False:
            print(dedent("""
            你跟着大部队来到了食堂门口，恭喜你，你们班今天又是最后一个吃饭。
            你叹了口气，听到身边有好多人在讨论着今天的坠楼事件。
            紧接着，宿管大喊了一声“安静”！声音变小了很多，你有些听不清了。
            不知道等了多久，你目送着甚至在你们班之后来的班级都已经进了食堂。
            “2班进！”
            终于走进食堂了！你跟着人流蜂拥而至排起了长队。
            打好饭路过食堂门口的时候，你看到几个老师站在一起面色凝重地说着什么。
            你放慢走路速度竖起耳朵听了听。
            “天台门不都锁着的吗？”
            “谁没看好钥匙？这么重要的东西能乱扔？”
            “钥匙都放保安室里的。”
            “监控呢？”
            “好像从昨天开始就坏了。”
            咦，似乎听到了什么意外的信息。
            你端着饭盘走到了座位上坐下，开始吃饭。
            大概是最后一个班的关系，食堂人陆陆续续都已经走光了。
            而今天纪律意外管得很严，老师都巡视着自己本班，有几个同学还因为说话被罚站了。
            没几个人说话，你没有听到什么重要的信息。
            """))
            System.clues['保安室钥匙丢失？'] = True
            if System.time_number == 12:
                return '宿舍'
            else:
                return '2班'
        else:
            print("食堂吃饭ing，由于纪律管得很严，没什么人说话，你没听到什么重要信息。")
            if System.time_number == 12:
                return '宿舍'
            else:
                System.classin = True
                return '2班'



class Dormitory(Scene):

    def enter(self):

        System.time_number += 1
        print(f"当前时间:{System.time_number}点")

        print(dedent("""
        到宿舍躺下后，宿管查完寝就关上了门。
        你为数不多的舍友今天因为生病请假了，宿舍里空荡荡的，你有点睡不着。
        看着门，你思索了一番，要不要出去呢？
        """))

        while True:
            action = input('>')

            if action == '出去':
                randomp = random.randint(0,1)

                if randomp == 0:
                    print(dedent("""
                    不，你怎么可能错过这种调查线索的好机会？
                    你偷偷下床走出宿舍，轻轻开门探出头环望四周。
                    没人，太好了!
                    你蹑手蹑脚走下楼梯，没想到迎面撞上一楼的宿管。
                    “干什么去？”她怀疑地盯着你质问道。
                    “呃……”，你尴尬的笑了笑，“上厕所……”
                    你心虚地快步走进厕所。
                    哈！睡觉去吧。
                    """))
                    System.classin = True
                    return '2班'

                elif randomp == 1:
                    print(dedent("""
                    不，你怎么可能错过这种调查线索的好机会？
                    你偷偷下床走出宿舍，轻轻开门探出头环望四周。
                    没人，太好了!
                    你蹑手蹑脚走下楼梯，运气很好，今天一楼的宿管居然不在。
                    该不会宿管上厕所去了吧？得赶紧趁这个机会溜走。
                    你加快步伐，尽量控制声音小跑出了宿舍门口。
                    """))
                    return '教学楼'

            elif action == '不出去':
                print(dedent("""
                算了，昨晚睡太晚了，太困了，还是睡觉吧，下午还要上课呢。
                你把被子盖在身上躺下了。
                """))
                System.classin = True
                return '2班'

            elif action == '菜单':
                clue_list = super().list()
                print(f"当前已收集线索：{clue_list}")
                print(f"当前时间:{System.time_number}点")

            else:
                print("不出去或出去？")



class WC(Scene):

    def enter(self):
        if System.time_number in [12, 13, 18]:
            print("厕所里没有人，换个地方吧。")
            return '教学楼'
        else:
            if System.clues['B同学在竞争中动用了关系？不正当竞争？'] == False and System.clues['A同学和B同学在竞争保送名额。'] == True:
                print(dedent("""
                你走到厕所隔间里关上门，无意中听到有人在谈论什么。
                “你知道吗？听说本来保送名额是A的！”
                “知道！听说最后A落选了，B保送了。”
                “嘘……劲爆的来了，B同学是走关系的！”
                “啊？真的————”
                “嘘！小声点……”
                它们渐渐走远了。
                似乎听到了什么额外的信息。
                """))
                System.clues['B同学在竞争中动用了关系？不正当竞争？'] = True
                return '教学楼'

            else:
                print("似乎没有什么线索可以收集。")
                return '教学楼'


class Building(Scene):

    def enter(self):
        System.classin = False
        print(dedent("""
        那么现在要去哪里探索呢？
        """))

        while True:
            action = input('>')

            if action == '1班':
                return '1班'

            elif action == '2班':
                return '2班'

            elif action == '3班':
                return '3班'

            elif action == '4班':
                return '4班'

            elif action == '办公室':
                return '办公室'

            elif action == '厕所':
                return '厕所'

            elif action == '结束':
                if System.time_number == 12:
                    return '宿舍'
                elif System.time_number in [13,14,15,16,17,18]:
                    System.classin = True
                    return '2班'
                elif System.time_number == 19:
                    System.time_number += 1
                    return '2班'


            elif action == '菜单':
                clue_list = super().list()
                print(f"当前已收集线索：{clue_list}")
                print(f"当前时间:{System.time_number}点")

            else:
                print("去1班，2班，3班，4班，厕所，办公室或者结束？")




class ClassRoom1(Scene):

    def enter(self):
        if System.clues['1班第5课是体育课。'] == False and System.clues['这场竞争最终以A同学的失败告终。A与B的关系不佳，B同学在1班。'] == True:
            print(dedent("""
            你走到1班门口，迎面碰上了自己的好友。
            从他的口中得知，1班第5节课是体育课。
            体育课也就意味着同学能够自如的出入教室，这是不是意味着什么？
            你似乎想到了什么。
            """))
            System.clues['1班第5课是体育课。'] = True
            return '教学楼'

        elif System.time_number in [12, 13, 18]:
            print("教室里没有人，换个地方吧。")
            return '教学楼'

        else:
            print("似乎没有什么线索可以收集。")
            return '教学楼'



class ClassRoom2(Scene):

    def enter(self):

        if System.time_number == 13 and System.classin == True:
            System.time_number += 1
            print(f"当前时间:{System.time_number}点")

            print(dedent("""
            下午第一节课是数学，上午的发生的事情一直环绕在你的脑海中。
            先是在家里睡得好好的突然穿越回了高中，然后紧接着还发生了坠楼案件。
            一切都巧合的有些奇怪，你努力在脑中回想着自己之前的高中时间线有没有发生类似的案件。
            如果曾经有发生过的话，那我应该印象很深啊？
            冤魂索命让我还原事件真相?你被自己脑海中的想法吓出了一声冷汗。
            “D，你来回答一下这题，为什么这道题要写范围？”
            你吓得一激灵，猛地站起了身，走神到十万八千里外的你看着满屏的数学计算迷茫不已。
            好家伙，果然好几年不学数学，连高中数学都费劲了，你很想穿越回时间线给自己两个巴掌。
            看你尴尬地站着沉默了半天，数学老师很不满意，她借此开始批评你和同学。
            你感觉有点不服气，发生了这种事和我本身有什么关系，怎么还人身攻击呢？
            很显然，老师并不知道在你身上发生了什么，但你始终感觉心里堵得慌。
            要不要尝试和老师说明情况呢？或许能争取到一点点理解？
            """))


            while True:
                action = input('>')

                if action == '不说':
                    print(dedent("""
                    算了，感觉老师只会把自己当笑话。
                    你无奈地耸耸肩，可能主角的命运就是这样吧，怎么能奢求凡人的理解？
                    站得腿有点酸，你用胳膊撑着桌子，终于熬到了下课。
                    """))
                    return '教学楼'

                elif action == '说':
                    print(dedent("""
                    “老师，不管你信不信，我实际上是穿越了，这大概是个梦吧。”
                    你说完这句话自己都感觉十分离谱，很显然，老师和同学也都是这么觉得的。
                    教室里哄堂大笑，“不想学没人逼你，编出这种荒唐的理由你自己信吗？”
                    我也想不信啊。
                    你叹了口气，移开了视线，几乎是顺理成章地滚到办公室罚站去了。
                    """))
                    return '办公室'

                elif action == '菜单':
                    clue_list = super().list()
                    print(f"当前已收集线索：{clue_list}")
                    print(f"当前时间:{System.time_number}点")

                else:
                    print("不说或说？")

        elif System.classin == True and System.time_number != 20:
            System.time_number += 1
            print(f"当前时间:{System.time_number}点")
            print("无聊的上课时间，你满脑子都在想着下一步应该去哪收集线索。")
            System.classin = False
            if System.time_number == 18:
                print("下课铃响了，又到吃饭时间了。这次吃不吃呢？")

                while True:
                    action = input('>')

                    if action == '不去':
                        randomp = random.randint(0,1)

                        if randomp == 0:
                            print(dedent("""
                            不，你怎么可能错过这种调查线索的好机会？
                            你趁着上厕所的功夫试图躲开排队，没想到今天不巧班主任点名。
                            他大喊着“人都来齐了再走”！
                            你叹了口气，站进了路队。
                            """))
                            return '食堂'

                        elif randomp == 1:
                            print(dedent("""
                            不，你怎么可能错过这种调查线索的好机会？
                            你趁着上厕所的功夫试图躲开排队，运气不错，没有老师点名。
                            等同学们都走光了，你从厕所探出了头环顾四周。
                            哈哈，现在是我的主场啦！
                            """))
                            return '教学楼'

                    elif action == '去':
                        print(dedent("""
                        有个道理是，人是铁，饭是钢。先吃饱肚子才能收集线索嘛。
                        你赞同地点点头，跟着路队下了楼。
                        """))
                        return '食堂'

                    elif action == '菜单':
                        clue_list = super().list()
                        print(f"当前已收集线索：{clue_list}")
                        print(f"当前时间:{System.time_number}点")

                    else:
                        if System.random_number != 1:
                            print("不__去？")
                            print("等等，为什么这个字都崩坏了？！")
                        else:
                            print("不去或去？")
            else:
                return '教学楼'

        elif System.clues['上午第5节课原本是信息课，因为信息老师有事临时调成了语文。' ] == True and System.clues['语文老师手机在第4节课下课后丢在2班没拿。'] == False:
            print(dedent("""
            下课了，你打算去问问本班同学有没有人清楚今天上午发生了什么。
            “啊，你不知道吗？”同学一脸疑惑地看着你，“你上午来了呀？第四节课语文课，你不记得了?
            下课他手机忘拿了，还是你送过去的。”
            你愣了一下。
            第4节课语文老师的手机是你送过去的，如果不送到办公室的话，是不是就可以岔开接电话的时间？
            你若有所思。
            """))
            System.clues['语文老师手机在第4节课下课后丢在2班没拿。'] = True
            System.classin = True
            return '教学楼'

        elif System.time_number in [12, 13, 18]:
            print("教室里没有人，换个地方吧。")
            return '教学楼'

        elif System.time_number == 20:
            print("整理线索的时间到！系统判断中……")
            clue_list = super().list()
            if len(clue_list) == 8:
                print("恭喜你！线索已全部收集完毕！")
                return '保安室'
            else:
                if System.random_number < 5:
                    print("线索没有收集完哦！再来一次吧！")
                    return 'Start'
                else:
                    return 'BE'

        else:
            print("很普通的下课时间，应该没什么可以收集的了。")
            return '教学楼'


class ClassRoom3(Scene):

    def enter(self):

        if System.time_number in [12, 13, 18]:
            print("教室里没有人，换个地方吧。")

        else:
            print("大家看起来气氛很压抑，还是不去打扰为好。")

        return '教学楼'

class ClassRoom4(Scene):

    def enter(self):
        if (
        not System.clues['这场竞争最终以A同学的失败告终。A与B的关系不佳，B同学在1班。']
        and System.clues['A同学和B同学在竞争保送名额。']
        and System.time_number not in [12, 13, 18]
        ):
            print(dedent("""
            你走到4班门口，迎面碰上了自己的好友。
            从她的口中得知，A同学据说由于争夺报录取名额失败，和B同学关系不佳。B同学在1班。
            也许应该去1班问问？或许能够知道什么信息。
            """))
            System.clues['这场竞争最终以A同学的失败告终。A与B的关系不佳，B同学在1班。'] = True
            return '教学楼'

        elif System.time_number in [12, 13, 18]:
            print("教室里没有人，换个地方吧。")
            return '教学楼'

        else:
            print("似乎没有什么线索可以收集。")
            return '教学楼'


class SecurityRoom(Scene):

    def enter(self):
        System.time_number = 22
        print(f"当前时间：{System.time_number}点")
        print(dedent("""
        你在宿舍躺下后再次睁开眼睛，发现自己正坐在教室里。
        教室很安静，偶尔能听到窸窸窣窣的声音，看起来正在上晚自习。
        这时，下课铃响了，宿管在门外喊着2班出来排队，同学们陆陆续续地走出教室。
        现在是什么时候？你有点疑惑地盯着眼前的一切，也许找个人问一下是一个不错的选择。
        “A同学？”旁边的同学被你问得一愣，“怎么突然问它？不知道，应该在3班吧。”
        他说着，往3班的方向望去，“喏，就是那边那个，看到没？”他指了指。
        你看到了一个背着书包靠在栏杆上的人，那人俯视着地面，不知道在想什么。
        看起来现在是死亡时间之前。
        你突然想起来保安室的钥匙似乎在前一天被拿走了，现在已经被那人拿到手了吗？
        你决定去看一下。跟着路队走下来的时候，你站到了最后一排，悄悄从后门溜走了。
        保安室灯亮着，但是居然没有人，这是很罕见的情况。
        你推开门走了进去，钥匙挂在了靠桌子的那面墙上。
        你注意到监控似乎有几个出现了故障，显示的是黑色的界面。
        要不要拿走钥匙？你犹豫了一下。
        这时，门外传来了聊天的对话声。
        保安回来了？
        你没办法再犹豫了，现在立即要做出选择。
        """))


        while True:
            action = input('>')

            if action == '拿':
                print(dedent("""
                你立刻拿走了挂着的钥匙。
                走出保安室时候，你注意到是几个走读的同学过来了，里面居然有A。
                A和你对视了一眼，走读的几个同学走到门口停下了。
                你从A身边走了过去。
                """))
                return 'HE'

            elif action == '不拿':
                print(dedent("""
                你犹豫了一下, 最终还是没拿走钥匙。
                走出保安室时候，你注意到是几个走读的同学过来了，里面居然有A。
                A和你对视了一眼，走读的几个同学走到门口停下了。
                你从A身边走了过去。
                """))
                return 'TE'

            elif action == '菜单':
                clue_list = super().list()
                print(f"当前已收集线索：{clue_list}")
                print(f"当前时间:{System.time_number}点")

            else:
                print("不拿或拿？")

class OfficeRoom(Scene):

    def enter(self):
        if System.time_number == 14 and System.clues['上午第5节课原本是信息课，因为信息老师有事临时调成了语文。'] = False:
            print(dedent("""
            你来到了办公室，运气很好的是，班主任居然不在座位上。
            你拿着书百无聊赖地靠墙站着，顺便听着办公室里的八卦。
            “xx又在骂骂咧咧了，还不是因为早上第5节课原本是信息课，结果临时换课了嘛。”
            “是快上课了才给他打电话，给他气得够呛，本来都在办公室睡着了。”
            早上第5节课是信息课？你皱起了眉头。
            如果能想个办法让语文老师接不到电话的话……是不是就可以趁着信息课溜出去了？
            下课铃响了，数学老师来到办公室，挥挥手示意你回班。
            """))
            System.clues['上午第5节课原本是信息课，因为信息老师有事临时调成了语文。'] = True
            return '教学楼'

        elif System.clues['A同学和B同学在竞争保送名额。'] == False:
            print(dedent("""
            进到办公室后，你沿着桌子的边缘走动，探头希望能看到什么有价值的信息。
            还真被你找到了，你发现了一个办公桌上摆着两份已经盖了章的文件, 似乎是关于高考保送的名额。
            其中一个名字正是今天出事的A同学，而另一个名字很陌生。
            B同学？你扫了一眼，默默记在了心里。
            """))
            System.clues['A同学和B同学在竞争保送名额。'] = True
            return '教学楼'

        else:
            print("好像没什么可以收集的了。")
            return '教学楼'

class BE(Scene):

    def enter(self):
        print(dedent("""
        你已经循环了很多次，却始终没有收集齐线索。
        最终，你被困在了这个循环之中。
        我的游戏设计得这么简单，能达到这个结局，你肯定是故意的吧？

        达成结局：循环
        """))
        exit(1)


class HE(Scene):

    def enter(self):
        print(dedent("""
        第二天睁眼，你照例完成了上午的课程。

        """))
        pass


class TE(Scene):

    def enter(self):
        pass



class Map(System):


    scenes = {
            '食堂': DiningRoom(),
            '宿舍' : Dormitory(),
            '厕所': WC(),
            '1班': ClassRoom1(),
            '2班': ClassRoom2(),
            '3班': ClassRoom3(),
            '4班': ClassRoom4(),
            '保安室': SecurityRoom(),
            '永恒': BE(),
            '救赎': HE(),
            '阴影': TE(),
            'Start': StartRoom(),
            '教学楼': Building(),
            '办公室': OfficeRoom()
            }

    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        defscene = Map.scenes.get(scene_name)
        return defscene

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('Start')
a_game = Engine(a_map)
a_game.play()
