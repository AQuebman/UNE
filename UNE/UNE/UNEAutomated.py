import random
from logging import exception
from builtins import input

class UNE:    
        
    def Pre_Conceived_Facts(self):
        self.KnownFacts = []
        i = 1
        while i < 99:
            a = input("List any Pre-conceived facts about this NPC:  ")
            self.KnownFacts.append(a)
            i+=1
            if a == '':
                break
        self.KnownFacts = list(filter(None, self.KnownFacts))
        print("Known Facts:  ", end='')
        print( ", ".join( repr(e) for e in self.KnownFacts)) 
    
    def What_NPC_Is(self):
        self.NPC_Modifier = ("Superfluous", "Addicted", "Conformist", "Nefarious", "Sensible", "Untrained", "Romantic", "Unreasonable", "Skilled", "Neglectful", "Lively", "Forthright", "Idealistic", "Unsupportive", "Rational", "Coarse", "Foolish", "Cunning", "Delightful", "Miserly", "Inept", "Banal", "Logical", "Subtle", "Reputable", "Wicked", "lazy", "Pessimistic", "Solemn", "Habitual", "Meek", "Helpful", "Unconcerned", "Generous", "Docile", "Cheery", "Pragmatic", "Serene", "Thoughtful", "Hopeless", "Pleasant", "Insensitive", "Titled", "Inexperienced", "Prying", "Oblivious", "Refined", "Indispensable", "Scholarly", "Conservative", "Uncouth", "Willful", "Indifferent", "Fickle", "Elderly", "Sinful", "Naive", "Privileged", "Glum", "Likable", "Lethargic", "Defiant", "Obnoxious", "Insightful", "Tactless", "Fanatic", "Plebeian", "Childish", "Pious", "Uneducated", "Inconsiderate", "Cultured", "Revolting", "Curious", "Touchy", "Needy", "Dignified", "Pushy", "Kind", "Corrupt", "Jovial", "Shrewd", "Liberal", "Compliant", "Destitute", "Conniving", "Careful", "Alluring", "Defective", "Optimistic", "Affluent", "Despondent", "Mindless", "Passionate", "Devoted", "Established", "Unseemly", "Dependable", "Righteous", "Confident")
        self.NPC_Noun = ('Gypsy', 'Witch', 'Merchant', 'Expert', 'Commoner', 'Judge', 'Ranger', 'Occultist', 'Reverend', 'Thug', 'Drifter', 'Journeyman', 'Statesman', 'Astrologer', 'Duelist', 'Jack-of-all-Trades', 'Aristocrat', 'Preacher', 'Artisan', 'Rogue', 'Missionary', 'Outcast', 'Mercenary', 'Caretaker', 'Hermit', 'Orator', 'Chieftain', 'Pioneer', 'Burglar', 'Vicar', 'Officer', 'Explorer', 'Warden', 'Outlaw', 'Adept', 'Bum', 'Sorcerer', 'Laborer', 'Master', 'Ascendant', 'Villager', 'Magus', 'Conscript', 'Worker', 'Actor', 'Herald', 'Highwayman', 'Fortune-Hunter', 'Governor', 'Scrapper', 'Monk', 'Homemaker', 'Recluse', 'Steward', 'Polymath', 'Magician', 'Traveler', 'Vagrant', 'Apprentice', 'Politician', 'Mediator', 'Crook', 'Civilian', 'Activist', 'Hero', 'Champion', 'Cleric', 'Slave', 'Gunman', 'Clairvoyant', 'Patriarch', 'Shopkeeper', 'Crone', 'Adventurer', 'Soldier', 'Entertainer', 'Craftsman', 'Scientist', 'Ascetic', 'Superior', 'Performer', 'Magister', 'Serf', 'Brute', 'Inquisitor', 'Lord', 'Villain', 'Professor', 'Servant', 'Charmer', 'Globetrotter', 'Sniper', 'Courtier', 'Priest', 'Tradesman', 'Hitman', 'Wizard', 'Beggar', 'Tradesman', 'Warrior')
        self.NPC_Creator = " ".join(['NPC: ', random.choice(self.NPC_Modifier), random.choice(self.NPC_Noun)])
        return(self.NPC_Creator)
        

    def NPC_Power(self):
        self.NPC_Power = input("Do you want to find out power level (Y/N)?  ").casefold()
        if (self.NPC_Power =='Y'.casefold() or self.NPC_Power == 'y'.casefold() or self.NPC_Power =='Yes'.casefold() or self.NPC_Power == "Yeah".casefold() or self.NPC_Power == "Yea".casefold()):
            self.Randomness_Level = input("Please select a Randomness_Level - 1: Order, 2: Calm, 3: Standard, 4: Disarray, 5: Chaos")
            self.Power_Level = random.randint(1,101)
            while True:
                try:
                            if self.Randomness_Level == '1':
                                if self.Power_Level in range(1, 3):
                                    print("NPC Power Level: ", end='')
                                    print("Much Weaker")
                                    break
                                elif self.Power_Level in range(3, 11):
                                    print("NPC Power Level: ", end='')
                                    print("Slightly Weaker")
                                    break                                    
                                elif self.Power_Level in range(11, 91):
                                    print("NPC Power Level: ", end='')
                                    print("Comparable")
                                    break                                    
                                elif self.Power_Level in range(91, 99):
                                    print("NPC Power Level: ", end='')
                                    print("Slightly Stronger")
                                    break                                    
                                elif self.Power_Level in range(99, 101):
                                    print("NPC Power Level: ", end='')
                                    print("Much Stronger")
                                    break                                    
                                else:
                                    print("Something went wrong")
                                    break
                                
                            elif self.Randomness_Level == '2':
                                if self.Power_Level in range(1, 5):
                                    print("NPC Power Level: ", end='')
                                    print("Much Weaker")
                                    break                                    
                                elif self.Power_Level in range(5, 16):
                                    print("NPC Power Level: ", end='')
                                    print("Slightly Weaker")
                                    break                                    
                                elif self.Power_Level in range(16, 86):
                                    print("NPC Power Level: ", end='')
                                    print("Comparable")
                                    break                                    
                                elif self.Power_Level in range(86, 97):
                                    print("NPC Power Level: ", end='')
                                    print("Slightly Stronger")
                                    break                                    
                                elif self.Power_Level in range(97, 101):
                                    print("NPC Power Level: ", end='')
                                    print("Much Stronger")
                                    break                                    
                                else:
                                    print("Something went wrong")
                                    break
                                
                            elif self.Randomness_Level == '3':
                                if self.Power_Level in range(1, 6):
                                    print("NPC Power Level: ", end='')
                                    print("Much Weaker")
                                    break                                    
                                elif self.Power_Level in range(6, 21):
                                    print("NPC Power Level: ", end='')
                                    print("Slightly Weaker")
                                    break                                    
                                elif self.Power_Level in range(21, 81):
                                    print("NPC Power Level: ", end='')
                                    print("Comparable")
                                    break                                    
                                elif self.Power_Level in range(81, 96):
                                    print("NPC Power Level: ", end='')
                                    print("Slightly Stronger")
                                    break                                    
                                elif self.Power_Level in range(96, 101):
                                    print("NPC Power Level: ", end='')
                                    print("Much Stronger")
                                    break                                    
                                else:
                                    print("Something went wrong")
                                    break
                                
                            elif self.Randomness_Level == '4':
                                if self.Power_Level in range(1, 9):
                                    print("NPC Power Level: ", end='')
                                    print("Much Weaker")
                                    break                                    
                                elif self.Power_Level in range(9, 26):
                                    print("NPC Power Level: ", end='')
                                    print("Slightly Weaker")
                                    break                                    
                                elif self.Power_Level in range(26, 76):
                                    print("NPC Power Level: ", end='')
                                    print("Comparable")
                                    break                                    
                                elif self.Power_Level in range(76, 93):
                                    print("NPC Power Level: ", end='')
                                    print("Slightly Stronger")
                                    break                                    
                                elif self.Power_Level in range(93, 101):
                                    print("NPC Power Level: ", end='')
                                    print("Much Stronger")
                                    break                                    
                                else:
                                    print("Something went wrong")
                                    break
                                
                            elif self.Randomness_Level == '5':
                                if self.Power_Level in range(1, 13):
                                    print("NPC Power Level: ", end='')
                                    print("Much Weaker")
                                    break                                    
                                elif self.Power_Level in range(13, 31):
                                    print("NPC Power Level: ", end='')
                                    print("Slightly Weaker")
                                    break                                    
                                elif self.Power_Level in range(31, 71):
                                    print("NPC Power Level: ", end='')
                                    print("Comparable")
                                    break                                    
                                elif self.Power_Level in range(71, 89):
                                    print("NPC Power Level: ", end='')
                                    print("Slightly Stronger")
                                    break                                    
                                elif self.Power_Level in range(89, 101):
                                    print("NPC Power Level: ", end='')
                                    print("Much Stronger")
                                    break                                    
                                else:
                                    print("Something went wrong")
                                    break
                            else:
                                self.Randomness_Level = input("Please select valid Randomness Level")
                except ValueError as exception:
                    print("Invalid Entries Try Again")                     
        else:
            pass
            
    def NPC_Motivation(self):
        self.motive = 0
        while self.motive < 3:
            self.motivation_verb = ('Advise', 'Obtain', 'Attempt', 'Spoil', 'Oppress', 'Interact', 'Create', 'Abduct', 'Promote', 'Conceive', 'Blight', 'Progress', 'Distress', 'Possess', 'Record', 'Embrace', 'Contact', 'Pursue', 'Associate', 'Prepare', 'Shepherd', 'Abuse', 'Indulge', 'Chronicle', 'Fulfill', 'Drive', 'Review', 'Aid', 'Follow', 'Advance', 'Guard', 'Conquer', 'Hinder', 'Plunder', 'Construct', 'Encourage', 'Agonize', 'Comprehend', 'Administer', 'Relate', 'Take', 'Discover', 'Deter', 'Acquire', 'Damage', 'Publicize', 'Burden', 'Advocate', 'Implement', 'Understand', 'Collaborate', 'Strive', 'Complete', 'Compel', 'Join', 'Assist', 'Defile', 'Produce', 'Institute', 'Account', 'Work', 'Accompany', 'Offend', 'Guide', 'Learn', 'Persecute', 'Communicate', 'Process', 'Report', 'Develop', 'Steal', 'Suggest', 'Weaken', 'Achieve', 'Secure', 'Inform', 'Patronize', 'Depress', 'Manager', 'Suppress', 'Proclaim', 'Operate', 'Access', 'Refine', 'Compose', 'Undermine', 'Explain', 'Discourage', 'Attend', 'Detect', 'Execute', 'Maintain', 'Realize', 'Convey', 'Rob', 'Establish', 'Overthrow', 'Support')
            self.motivation_noun = ('Wealth', 'Hardship', 'Affluence', 'Resources', 'Prosperity', 'Poverty', 'Opulence', 'Deprivation', 'Success', 'Distress', 'Contraband', 'Music', 'Literature', 'Technology', 'Alcohol', 'Medicines', 'Beauty', 'Strength', 'Intelligence', 'Force', 'The Wealthy', 'The Populous', 'Enemies', 'The Public', 'Religion', 'The Poor', 'Family', 'The Elite', 'Academia', 'The Forsaken', 'The Law', 'The Government', 'The Oppressed', 'Friends', 'Criminals', 'Allies', 'Secret Societies', 'The World', 'Military', 'The Church', 'Dreams', 'Discretion', 'Love', 'Freedom', 'Pain', 'Faith', 'Slavery', 'Enlightenment', 'Racism', 'Sensuality', 'Dissonance', 'Peace', 'Discrimination', 'Disbelief', 'Pleasure', 'Hate', 'Happiness', 'Servitude', 'Harmony', 'Justice', 'Gluttony', 'Lust', 'Envy', 'Greed', 'Laziness', 'Wrath', 'Pride', 'Purity', 'Moderation', 'Vigilance', 'Zeal', 'Composure', 'Charity', 'Modesty', 'Atrocities', 'Cowardice', 'Narcissism', 'Compassion', 'Valor', 'Patience', 'Advice', 'Propaganda', 'Science', 'Knowledge', 'Communications', 'Lies', 'Myths', 'Riddles', 'Stories', 'Legends', 'Industry', 'New Religions', 'Progress', 'Animals', 'Ghosts', 'Magic', 'Nature', 'Old Religions', 'Expertise', 'Spirits')
            self.FullMotivation = " ".join(['(',random.choice(self.motivation_verb), random.choice(self.motivation_noun), ',', random.choice(self.motivation_verb), random.choice(self.motivation_noun), ',', random.choice(self.motivation_verb), random.choice(self.motivation_noun),')'])
            self.motive+=1
        return(self.FullMotivation)
            
    def OUTPUT(self):
        self.OUTPUT = NPC.What_NPC_Is() + NPC.NPC_Motivation()
        print(self.OUTPUT)
            
if __name__ == '__main__':
    NPC = UNE()
    NPC.Pre_Conceived_Facts()
    NPC.What_NPC_Is()
    NPC.NPC_Power()
    NPC.NPC_Motivation()
    NPC.OUTPUT()