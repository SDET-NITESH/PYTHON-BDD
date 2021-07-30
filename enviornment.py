"""Environment File Setup"""

def before_feature(context, feature):
    context.feature = feature



def before_tag(context, tag):

    if tag.lower().startswith("functional-scenario"):
        pass
    elif tag.lower().startswith("data"):
        pass
    elif tag.lower().startswith("negative-scenario"):
        pass




# def after_feature(context, feature):
#     if len(context.append_list)>0:
#         print(context.append_list)




#















