def Adventure():
    name =  input("Hello traveller! What is your name? ")
    beginning = input(f"Greetings {name}! Would you like to go on a adventure? ")
    if beginning.strip().lower() != "yes":
        print(f"Thats ok {name}. Come adventure another day.")
        return
    
    Fail_Message = "Sorry that's not a valid choice. You lose."

    print("Alright lets begin")
    print("You are walking along a dirt path trying to find shelter before dark. As the sunset dyes the sky orange you quicken your pace.")
    print("You come across a fork in the road. One way leads off into a meadow of flowers and the other leads into a dense forest. ")
    answer1 = input("Do you go into the Meadow or the Forest? ").lower()

    if answer1 == "forest":
        print("Going into the dense forest so close to dark turns out to be a bad idea. The thick trees smother nearly all light making it difficult to see the path in front of you.")
        Direction = input("Now nearly blind you have choice; Go Back the way you came or continue Forward. Back or Forward.").lower()
        if Direction == "back":
            print("Afraid of losing your way you decided to turn back but in your attempt to reorient yourself back the way you came you only manage to make yourslef more lost.")
            print("You wander off the trail and trip over a root. You blindly flail and break your neck killing you. You lose.")
            return
        elif Direction == "forward":
            print("Continuing deeper into the forest you see a hut perched in the middle of clearing. You can see lights in the windows but you can't tell if anyone is home.")
            Hut = input("Do you walk up to the hut and Knock on the door or continue Forward? ").lower()
            if Hut == "forward":
                print("You chose to fend for yourself and walk deeper into the woods. As the light of the hut fades you are ambushed by a pack of wolves and are torn to shreds. You lose.")
                return
            elif Hut == "knock":
                print(f"You knock on the door and from inside you hear a weezing cackle. 'Come in {name}. It's nice and warm.'" )
                inside = input("Do you chose to go Inside or Continue on your path? ").lower()
                if inside == "continue":
                    print("You chose to fend for yourself and walk deeper into the woods. As the light of the hut fades you are ambushed by a pack of wolves and are torn to shreds. You lose.")
                    return
                elif inside == "inside":
                    print("You gingerly open the door and you see an old woman in rocking chair facing a fire with her back to you.")
                    print("Near the window is a makeshift kitchen with a knife resting on a cutting board.")
                    Knife = input("Do you take the knife? Yes or No? ").lower()
                    if Knife == "yes":
                        print("You stow the knife and walk towards her.")
                    elif Knife == "no":
                        print("You glance away from the kitchen and walk towards her")
                    else:
                        print(Fail_Message)
                        return
                    print("As you walk foward the old woman turns to face you and smiles. You ask her 'Who are you?'")
                    print("'Oh nobody of consequence my dearie. Just a traveller you see.' She stands up from her rocking chair. 'Yes I came here to sample the finest delicacies'")
                    input("'For instance, dumb adventurures like YOU!' She lunges forward, her gnarled fingers clawing through your flesh like a warm blade through butter. ").lower()
                    if Knife == "no":
                        print("Your fists bounce harmlessly off of her body as she claws you open. As your conciouness fades you see her shove hanfulls of your oragans into her mouth cackling as she works. You lose.")
                        return
                    if Knife == "yes":
                        input("You reach for your stowed blade and stab straight through her eye. She gargles out one more wheezy sound of confusion and then goes limp.")
                        print("You push her body off of you as breath a sigh of relief. You managed to survive.")
                        input("You curl up in the warm safety of the hut and rest up for any adventures the may come tommorow.")
                        print("Congratulations! You survived the night! Play again and see if you get a different ending.")
                        return
                        

        else:
            print(Fail_Message)
            return
    elif answer1 == "meadow":
        print("You stroll along the road through the meadow. You spot a patch of beatiful red flowers.")
        sniff = input("Do you stop to take a sniff? Yes or No ").lower()
        if sniff == "yes":
            print("A bee suddenly flies out of the flower and stings you on the nose. You die of anaphylactic shock. You lose")
            return
        elif sniff == "no":
            print("You keep your brisk pace through the meadow enjoying the sights and sounds of nature.")
            print("As you crest over the hill you see a quaint village off the beaten path.")
            Village = input("Do you stay on the Path or veer off towards the Village? ").lower()
            if Village == "village":
                print("You walk into the village. The village is bustling, trying to get all their work done before nightfall. At the very far end of town you see large manor loom over the rest of the buildings.")
                Question = input("The villagers seem nervous for some reason. Do you go ask them why? Yes or No? ").lower()
                if Question == "yes":
                    print("A disheveled village quickly whispers out an answer'You don't wanna be out here after curfew. Find somewhere to stay before dark' before shuffling off.")
                    print("Realizing the position of the sun you quickly move into the nearest establishment; a carpenter.")
                    input("You glance outside as darkness falls and you see a man in what appears to be a tuxedo run out from the large manor. As he sprints through town you see he is wearning a strange stone mask.") 
                    print("Looking ahead at where he is going you see his target, a man figeting with a pair a keys struggling to get the door to his home open.")
                    print("In the blink of an eye the man has a sword through his head with blinding speed. Yet the strange man continues, throwing off his mask and sticking his face into the mans neck. In an instant the man dries up like a prune.")
                    Stake = input("A vampire! Do you use the carpenters tools at make a stake or just rest for the night and get ready to leave in the morning? Stake or Rest").lower()
                    if Stake == "rest":
                        print("You decide to simply sleep, after all you don't know these people and have no reason to help.")
                        print("You wake up the next morning and leave town.")
                        print("Congratulations! You survived the night. Play again to see if you get a different ending.")
                    if Stake == "stake":
                        Kill = input("You rush outside with your stake and the vampires head snaps towards you. You ready yourself as he begins to charge. As he readies his blade you prepare to act. Do you try to Dodge or try to go for the Kill? ").lower()
                        if Kill == "kill":
                            print("You lunge forward with all your might and try to drive the stake into the vampires heart. However its sword is faster than your stake. Before even touching the vampires skin his sword slices your head clean off. You lose")
                            return
                        if Kill == "dodge":
                            print("You slide under the vampires attack sending the creature off balance. With a uppercut you slam the stake into its heart.")
                            input("The townsfolk rush out and thank you for saving them. You spend the rest of the night drinking and eating before the exhuastion of the day finally sets in.")
                            print("Congratulations! You survived the night. Play again to see if you get a different ending.")
                            return
                    else:
                        print(Fail_Message)
                        return

                elif Question == "no":
                    print("You continue wandering through town as you look for a place to stay. As the sun sinks below the horizon the doors of the large burst open as a man wearning a suit and mask sprints out weilding a sword.")
                    print("Before you can get a word out he closes the distance to you and sends a blade into your brain. You lose")
                    return
                else:
                    print(Fail_Message)
                    return
            elif Village == "path":
                input("Being the smart adventurer you are, you decude to not get involved in any adventures.")
                print("You find a place to rest in the meadow and go to sleep.")
                print("Congratulations! You survived the night! Play again and see if you get a different ending.")

        
                
        
            
Adventure()
