import sims4.commands
#Actually I'm not sure, but I think Live means this order can be used in live model.
@sims4.commands.Command('helloworld', command_type=sims4.commands.CommandType.Live)
def hellow(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output('Hello human')
