basic_strategy_hard = { #Dealer Card: {HandValue:Play},{HandValue:Play},...
        2: {4:"H",5:"H",6:"H",7:"H",8:"H",9:"H",10:"D",11:"D",12:"H",13:"S",14:"S",15:"S",16:"S",17:"S",18:"S",19:"S",20:"S",21:"S"},
        3: {4:"H",5:"H",6:"H",7:"H",8:"H",9:"D",10:"D",11:"D",12:"H",13:"S",14:"S",15:"S",16:"S",17:"S",18:"S",19:"S",20:"S",21:"S"},
        4: {4:"H",5:"H",6:"H",7:"H",8:"H",9:"D",10:"D",11:"D",12:"S",13:"S",14:"S",15:"S",16:"S",17:"S",18:"S",19:"S",20:"S",21:"S"},
        5: {4:"H",5:"H",6:"H",7:"H",8:"H",9:"D",10:"D",11:"D",12:"S",13:"S",14:"S",15:"S",16:"S",17:"S",18:"S",19:"S",20:"S",21:"S"},
        6: {4:"H",5:"H",6:"H",7:"H",8:"H",9:"D",10:"D",11:"D",12:"S",13:"S",14:"S",15:"S",16:"S",17:"S",18:"S",19:"S",20:"S",21:"S"},
        7: {4:"H",5:"H",6:"H",7:"H",8:"H",9:"H",10:"D",11:"D",12:"H",13:"H",14:"H",15:"H",16:"H",17:"S",18:"S",19:"S",20:"S",21:"S"},
        8: {4:"H",5:"H",6:"H",7:"H",8:"H",9:"H",10:"D",11:"D",12:"H",13:"H",14:"H",15:"H",16:"H",17:"S",18:"S",19:"S",20:"S",21:"S"},
        9: {4:"H",5:"H",6:"H",7:"H",8:"H",9:"H",10:"D",11:"D",12:"H",13:"H",14:"H",15:"H",16:"H",17:"S",18:"S",19:"S",20:"S",21:"S"},
        10:{4:"H",5:"H",6:"H",7:"H",8:"H",9:"H",10:"H",11:"D",12:"H",13:"H",14:"H",15:"H",16:"H",17:"S",18:"S",19:"S",20:"S",21:"S"},
        11:{4:"H",5:"H",6:"H",7:"H",8:"H",9:"H",10:"H",11:"D",12:"H",13:"H",14:"H",15:"H",16:"H",17:"S",18:"S",19:"S",20:"S",21:"S"},
        }


#Adding white space for dealers card x to lineup with 2x 
#Makes doing substitutions by line number easier in Vim




basic_strategy_soft = { #Dealer Card: {HandValue:Play},{HandValue:Play},...
        2: {13:"H",14:"H",15:"H",16:"H",17:"H",18:"D",19:"S",20:"S",21:"S"},
        3: {13:"H",14:"H",15:"H",16:"D",17:"D",18:"D",19:"S",20:"S",21:"S"},
        4: {13:"H",14:"H",15:"D",16:"D",17:"D",18:"D",19:"S",20:"S",21:"S"},
        5: {13:"D",14:"D",15:"D",16:"D",17:"D",18:"D",19:"S",20:"S",21:"S"},
        6: {13:"D",14:"D",15:"D",16:"D",17:"D",18:"D",19:"D",20:"S",21:"S"},
        7: {13:"H",14:"H",15:"H",16:"H",17:"H",18:"S",19:"S",20:"S",21:"S"},
        8: {13:"H",14:"H",15:"H",16:"H",17:"H",18:"S",19:"S",20:"S",21:"S"},
        9: {13:"H",14:"H",15:"H",16:"H",17:"H",18:"H",19:"S",20:"S",21:"S"},
        10:{13:"H",14:"H",15:"H",16:"H",17:"H",18:"H",19:"S",20:"S",21:"S"},
        11:{13:"H",14:"H",15:"H",16:"H",17:"H",18:"H",19:"S",20:"S",21:"S"},
        }





#Table only used to decide if to split and then passed to tables above
#Assumes DAS is allowed
#P = split, N = nosplit 
basic_strategy_split = { #Dealer Card: {HandValue:Play},{HandValue:Play},... 
        2: {4:"P",6:"P",8:"N",10:"N",12:"P",14:"P",16:"P",18:"N",20:"N",22:"P"},
        3: {4:"P",6:"P",8:"N",10:"N",12:"P",14:"P",16:"P",18:"N",20:"N",22:"P"},
        4: {4:"P",6:"P",8:"N",10:"N",12:"P",14:"P",16:"P",18:"N",20:"N",22:"P"},
        5: {4:"P",6:"P",8:"N",10:"P",12:"P",14:"P",16:"P",18:"N",20:"N",22:"P"},
        6: {4:"P",6:"P",8:"N",10:"P",12:"P",14:"P",16:"P",18:"N",20:"N",22:"P"},
        7: {4:"P",6:"P",8:"N",10:"N",12:"N",14:"P",16:"P",18:"N",20:"N",22:"P"},
        8: {4:"N",6:"N",8:"N",10:"N",12:"N",14:"N",16:"P",18:"N",20:"N",22:"P"},
        9: {4:"N",6:"N",8:"N",10:"N",12:"N",14:"N",16:"P",18:"N",20:"N",22:"P"},
        10:{4:"N",6:"N",8:"N",10:"N",12:"N",14:"N",16:"P",18:"N",20:"N",22:"P"},
        11:{4:"N",6:"N",8:"N",10:"N",12:"N",14:"N",16:"P",18:"N",20:"N",22:"P"},
        }
