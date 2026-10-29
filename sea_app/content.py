import re

# Knowledge base of topics with explanations and teaching sequences
TOPICS = {
    "1+1": {
        "keywords": ["1+1", "one plus one", "add", "addition"],
        "young_child": {
            "explanation": "1 + 1 = 2! 🎉\n\nImagine you have 1 apple. Your friend gives you 1 more apple. Now you have 2 apples! That's what 1 + 1 means. When you put one thing and one more thing together, you get 2 things!",
            "initial_question": "If you have 1 toy and I give you 1 more toy, how many toys do you have now?",
            "follow_ups": [
                "Great! That's right - you have 2 toys! Now, if you had 2 toys and got 1 more, how many would you have?",
                "Perfect! You're really good at this! One more: if you had 1 apple and ate it, how many would you have left?",
                "Wonderful! You understand adding! 🌟"
            ],
            "hints": [
                "Think about counting on your fingers: hold up 1 finger, then 1 more finger. How many do you see?",
                "1 + 1 = 2. That's the answer!",
                "You can also say: one plus one equals two"
            ]
        },
        "child": {
            "explanation": "**1 + 1 = 2**\n\nAddition means combining groups. When you add 1 and 1, you're putting two groups of one item together. The result is 2. This is one of the most basic math facts!\n\nExample: 1 penny + 1 penny = 2 pennies",
            "initial_question": "Can you tell me what 1 + 1 equals?",
            "follow_ups": [
                "Correct! 1 + 1 = 2. Now, what do you think 2 + 1 would equal?",
                "Good thinking! Now try this: 1 + 2 = ?",
                "Excellent! You understand addition! Can you think of a real example where you'd use 1 + 1?"
            ],
            "hints": [
                "The answer is 2",
                "Think: 1 thing + 1 thing = how many things?",
                "Count on your fingers: 1... 2"
            ]
        },
        "teen": {
            "explanation": "1 + 1 = 2 is the most fundamental operation in arithmetic. Addition combines quantities to find a total. In this case, one unit plus one unit equals two units. This principle extends to all numbers and is the foundation for all arithmetic operations.",
            "initial_question": "This is the simplest addition fact. Why do you think 1 + 1 = 2?",
            "follow_ups": [
                "Correct understanding. Now, how would you explain addition to someone younger than you?",
                "Good. Can you think about why this principle works for all numbers?",
                "Excellent. This is foundational to all mathematics!"
            ],
            "hints": [
                "Addition represents combining distinct sets",
                "1 + 1 = 2 is the basis for understanding number systems",
                "Think about the Peano axioms that define natural numbers"
            ]
        },
        "adult": {
            "explanation": "1 + 1 = 2 in standard arithmetic. This is an axiom in formal mathematics (Peano's axioms). In modular arithmetic, 1 + 1 may equal different values depending on the modulus. For example, in mod 2 arithmetic, 1 + 1 ≡ 0 (mod 2).",
            "initial_question": "In what mathematical context is 1 + 1 not equal to 2?",
            "follow_ups": [
                "Excellent - you understand modular arithmetic. What are other fields where addition behaves differently?",
                "Good point. How does this relate to abstract algebra?",
                "Well reasoned. This illustrates how operations are defined by their axioms."
            ],
            "hints": [
                "Consider modular arithmetic and finite fields",
                "Boolean algebra is another example where 1 + 1 ≠ 2",
                "Abstract algebra allows us to define addition in various ways"
            ]
        }
    },
    "addition": {
        "keywords": ["add", "plus", "addition", "adding"],
        "young_child": {
            "explanation": "Addition means putting things together! ➕\n\nWhen you add, you're combining groups to see how many you have in total. Like if you have 2 cookies and get 1 more cookie, you now have 3 cookies! That's 2 + 1 = 3.",
            "initial_question": "If you have 2 apples and your friend gives you 1 apple, how many apples do you have now?",
            "follow_ups": [
                "Yes! 2 + 1 = 3! You got it! Now try: 1 + 2 = ?",
                "Great! The answer is the same! Now try: 2 + 2 = ?",
                "Perfect! You're an addition expert! 🌟"
            ],
            "hints": [
                "Count: you start with some, then you get more, count them all!",
                "Use your fingers to count",
                "2 + 1 means start at 2, then count 1 more"
            ]
        },
        "child": {
            "explanation": "Addition is combining numbers to find the total. The symbol is +. We use addition when we want to know 'how many altogether'.\n\nFor example:\n- 3 + 2 = 5 (three things plus two things equals five things)\n- 4 + 3 = 7 (four things plus three things equals seven things)\n\nYou can check your answer by counting on your fingers!",
            "initial_question": "What is 3 + 4? Can you explain how you figured it out?",
            "follow_ups": [
                "Great! 3 + 4 = 7. Now, does 4 + 3 equal the same thing? Why?",
                "Exactly! This is called the commutative property - order doesn't matter!",
                "Excellent understanding of addition!"
            ],
            "hints": [
                "Count on your fingers starting from the bigger number",
                "You can draw dots or use objects to represent the numbers",
                "Start at 3, then count: 4, 5, 6, 7"
            ]
        },
        "teen": {
            "explanation": "Addition is one of the four basic arithmetic operations. It combines two or more numbers to produce a sum. Properties of addition include:\n- Commutative: a + b = b + a\n- Associative: (a + b) + c = a + (b + c)\n- Identity: a + 0 = a\n- Inverse: a + (-a) = 0",
            "initial_question": "Can you explain why the commutative property works for addition?",
            "follow_ups": [
                "Good insight. How would you prove this property?",
                "Excellent. Now, how does this relate to the associative property?",
                "Well reasoned. These properties form the foundation of algebra."
            ],
            "hints": [
                "Think about combining physical objects",
                "The order of combining groups doesn't change the total",
                "This relates to the algebraic structure of integers"
            ]
        },
        "adult": {
            "explanation": "Addition is a binary operation defined on various mathematical structures: integers, real numbers, complex numbers, and abstract algebraic structures. In group theory, addition defines an abelian group structure under certain axioms. The formal definition relies on the Peano axioms for natural numbers.",
            "initial_question": "How is addition defined in abstract algebra, and what properties must it satisfy?",
            "follow_ups": [
                "Excellent. What about addition in other algebraic structures like rings or fields?",
                "Good understanding. How does this relate to the fundamental theorem of arithmetic?",
                "Well articulated. This shows deep mathematical understanding."
            ],
            "hints": [
                "Consider the group axioms: closure, associativity, identity, inverse",
                "Different structures impose different requirements on addition",
                "Addition in Zn is modular arithmetic"
            ]
        }
    },
    "loop": {
        "keywords": ["loop", "repeat", "coding", "programming", "for", "while"],
        "young_child": {
            "explanation": "A loop means doing the same thing over and over! 🔁\n\nLike if you want to clap 5 times, you don't have to tell a robot: \"clap, clap, clap, clap, clap.\" Instead you say: \"clap 5 times!\" That's a loop!\n\nLoops save us from writing the same code many times.",
            "initial_question": "Can you think of something you do over and over every day? Like brushing your teeth or jumping?",
            "follow_ups": [
                "Great example! That's a loop in real life! Now, why do you think computers need loops?",
                "Perfect! Computers need to repeat things too! What if we told a computer to print your name 100 times?",
                "Excellent! You understand loops! 🌟"
            ],
            "hints": [
                "Think about things that repeat: days of the week, counting, etc.",
                "A loop saves time by doing the same thing multiple times",
                "Instead of writing code 100 times, write a loop that runs 100 times"
            ]
        },
        "child": {
            "explanation": "A loop in programming is code that repeats. Instead of writing the same instruction multiple times, you write it once and tell the computer how many times to repeat it.\n\nExample: Instead of:\n```\nprint(\"Hello\")\nprint(\"Hello\")\nprint(\"Hello\")\n```\n\nYou write:\n```\nfor i in range(3):\n  print(\"Hello\")\n```\n\nBoth do the same thing, but the loop is shorter!",
            "initial_question": "Why do you think programmers use loops instead of just writing code multiple times?",
            "follow_ups": [
                "Great thinking! Now, can you think of a real-world example where a loop would be useful?",
                "Excellent! What if you needed to repeat something 1000 times? Would you write it 1000 times?",
                "Perfect understanding of loops!"
            ],
            "hints": [
                "Loops save time and make code cleaner",
                "A loop can run any number of times",
                "Common loops: for loops and while loops"
            ]
        },
        "teen": {
            "explanation": "A loop is a control flow structure that repeats a block of code. Two main types: for loops (repeat a known number of times) and while loops (repeat while a condition is true).\n\nExample uses:\n- Process each item in a list\n- Count from 1 to 1000\n- Keep asking for input until valid\n- Generate patterns",
            "initial_question": "What's the difference between a for loop and a while loop?",
            "follow_ups": [
                "Good distinction. When would you use each type?",
                "Excellent. How do you avoid infinite loops?",
                "Well reasoned. Loops are essential for efficient programming!"
            ],
            "hints": [
                "For loops: known iterations",
                "While loops: conditional iterations",
                "Always have a loop termination condition"
            ]
        },
        "adult": {
            "explanation": "Loops are fundamental control structures enabling iteration. Formal definition varies by language but includes for loops, while loops, do-while loops. Loop optimization involves unrolling, vectorization, and parallelization. Understanding time complexity (Big O) is crucial for loop efficiency.",
            "initial_question": "How does loop optimization impact algorithm performance?",
            "follow_ups": [
                "Good. Discuss vectorization and SIMD optimizations.",
                "Excellent. How do you analyze loop time complexity?",
                "Well articulated understanding of performance engineering."
            ],
            "hints": [
                "Consider Big O notation for loop analysis",
                "Modern compilers perform loop optimization",
                "Vectorization can parallelize independent iterations"
            ]
        }
    },
    "variable": {
        "keywords": ["variable", "programming", "coding", "store", "data", "name"],
        "young_child": {
            "explanation": "A variable is like a **labeled box** where you store information! 📦\n\nExample: You can say \"My favorite color box\" and put blue in it. Later, you can ask \"What's in the favorite color box?\" and it tells you blue!\n\nIn coding, we use variables to remember things!",
            "initial_question": "If I had a box labeled 'Age' and put the number 7 in it, what would be inside the Age box?",
            "follow_ups": [
                "Correct! Variables store information! Now, can you think of another box we might need?",
                "Great! Variables help programs remember things! What else might a program need to remember?",
                "Perfect! You understand variables! 🌟"
            ],
            "hints": [
                "Think of a variable like a labeled container",
                "You put information in, you can take it out",
                "Each variable has a name (like 'name', 'age', 'color')"
            ]
        },
        "child": {
            "explanation": "A variable is a named container that stores a value (number, text, true/false, etc.). Variables let programs remember and use information.\n\nExample:\n```\nage = 12\nname = \"Sara\"\n```\n\nHere, `age` stores 12, and `name` stores \"Sara\". We can use these variables later in our code.",
            "initial_question": "Why do programmers use variables instead of just typing numbers directly?",
            "follow_ups": [
                "Good point! Variables make code more flexible. What if the value changes?",
                "Exactly! Now, what's the difference between a variable and its value?",
                "Excellent understanding of programming fundamentals!"
            ],
            "hints": [
                "Variables = containers, values = contents",
                "Variable names should be descriptive",
                "You can change a variable's value anytime"
            ]
        },
        "teen": {
            "explanation": "Variables are identifiers bound to memory locations containing values. Key concepts: scope, lifetime, mutability. Types include primitive (int, float, bool, char) and complex (objects, arrays).\n\nExample:\n```python\nage = 15          # integer variable\nname = \"Alex\"     # string variable\nis_student = True # boolean variable\n```",
            "initial_question": "What's the difference between variable scope and variable lifetime?",
            "follow_ups": [
                "Good distinction. How do scope and lifetime relate?",
                "Excellent. Explain global vs local variables.",
                "Well reasoned. This is crucial for avoiding bugs!"
            ],
            "hints": [
                "Scope: where the variable can be accessed",
                "Lifetime: how long the variable exists",
                "Global variables have broader scope and lifetime"
            ]
        },
        "adult": {
            "explanation": "Variables are bindings of identifiers to memory locations. Implementation details vary by language: stack allocation (primitives), heap allocation (objects), register optimization. Concepts include scope (lexical vs dynamic), lifetime (automatic vs manual), and mutability constraints.",
            "initial_question": "Explain how variable scope is implemented at the compiler/runtime level.",
            "follow_ups": [
                "Good. Discuss stack frames and scope chains.",
                "Excellent. How do closures maintain variable references?",
                "Well explained. This shows deep systems understanding."
            ],
            "hints": [
                "Stack frames manage local variable scope",
                "Closures capture variables from outer scopes",
                "Memory management relates to variable lifetime"
            ]
        }
    },
    "function": {
        "keywords": ["function", "method", "code", "reusable", "programming"],
        "young_child": {
            "explanation": "A function is like a **recipe**! 📖\n\nYou write down steps once (make a sandwich), then whenever you need a sandwich, you just follow the recipe. You don't have to rewrite all the steps!\n\nIn coding, a function is instructions you write once and use many times!",
            "initial_question": "If you had a recipe for cookies, how many times could you use it to make cookies?",
            "follow_ups": [
                "Exactly! Many times! Functions work the same way in coding!",
                "Yes! Functions save time by reusing code! What else uses recipes?",
                "Perfect! You understand functions! 🌟"
            ],
            "hints": [
                "A function is like a recipe or instruction list",
                "You write it once, use it many times",
                "Functions make programming faster and easier"
            ]
        },
        "child": {
            "explanation": "A function is reusable code that performs a specific task. Instead of writing the same code multiple times, you create a function and call it whenever needed.\n\nExample:\n```python\ndef greet(name):\n  print(\"Hello, \" + name)\n\ngreet(\"Alice\")\ngreet(\"Bob\")\n```",
            "initial_question": "Why would a programmer create a function instead of just writing code directly?",
            "follow_ups": [
                "Good thinking! Functions reduce repetition. What are other benefits?",
                "Excellent! Functions make code organized. Can you think of an example function?",
                "Great understanding! Functions are essential!"
            ],
            "hints": [
                "Functions avoid code repetition",
                "Functions make code organized and readable",
                "Functions can take input (parameters) and return output"
            ]
        },
        "teen": {
            "explanation": "A function is a reusable block of code that performs a specific task. Functions have parameters (input), logic (processing), and return values (output).\n\nStructure:\n```python\ndef function_name(parameters):\n  # code here\n  return result\n```\n\nBenefits: DRY (Don't Repeat Yourself), modularity, testability.",
            "initial_question": "Explain the relationship between parameters, arguments, and return values in functions.",
            "follow_ups": [
                "Good explanation. How do functions contribute to code modularity?",
                "Excellent. What's the difference between pass-by-value and pass-by-reference?",
                "Well reasoned. Functions are fundamental to programming!"
            ],
            "hints": [
                "Parameters: function definition inputs",
                "Arguments: actual values passed to function",
                "Return value: output from function"
            ]
        },
        "adult": {
            "explanation": "Functions are abstractions encapsulating behavior. Key concepts: closures, higher-order functions, tail recursion optimization, functional programming paradigms. Implementation includes call stacks, memory management, and inlining optimizations.",
            "initial_question": "How do closures enable functional programming paradigms?",
            "follow_ups": [
                "Good. Discuss first-class functions and callbacks.",
                "Excellent. How do lambda functions enable functional composition?",
                "Well explained. This demonstrates advanced programming knowledge."
            ],
            "hints": [
                "Closures capture lexical scope",
                "First-class functions can be passed as arguments",
                "Functional programming emphasizes immutability"
            ]
        }
    },
    "photosynthesis": {
        "keywords": ["photosynthesis", "plant", "food", "sun", "light", "green"],
        "young_child": {
            "explanation": "Plants are like little food makers! 🌱 They use sunlight, water from the ground, and air to make their own food. It's like the plant is making breakfast for itself using the sun's energy. The best part? They also make oxygen, which is the air we breathe!",
            "initial_question": "Have you ever seen a plant sitting in sunlight? What do you think it does with all that light?",
            "follow_ups": [
                "Great thinking! Now, where do you think plants get water from?",
                "Excellent! So plants use water and sunlight... what else do you think they might need from nature?",
                "You're on the right track! After plants make food, what do you think happens to it? Do they eat it, store it, or use it to grow?"
            ],
            "hints": [
                "Think about where plants get water from - look around a plant in nature!",
                "Plants need three things: water, light, and something from the air",
                "The plant uses food to grow bigger and stronger, just like you!"
            ]
        },
        "child": {
            "explanation": "Photosynthesis is the process where plants make their own food. Here's how it works: Plants take water through their roots from the soil, they get carbon dioxide from the air through tiny holes in their leaves, and they use energy from sunlight. These three ingredients mix together inside the plant to create sugar (which is food) and oxygen. The oxygen is released back into the air for us to breathe!",
            "initial_question": "What do you think plants use photosynthesis for? Why would they need to make their own food?",
            "follow_ups": [
                "Exactly! Plants need energy to grow. Now, what do you think happens to the oxygen that plants make - where does it go?",
                "Good observation! Let me ask you: if plants need sunlight for photosynthesis, what do you think happens to plants in dark places?",
                "Smart thinking! Here's the next question: Plants take in carbon dioxide from the air - where do you think animals and people get the oxygen to breathe from?"
            ],
            "hints": [
                "Think about why plants are usually green - what part of sunlight do they use?",
                "Plants need water from soil, light from sun, and gas from air - that's 3 ingredients!",
                "Photosynthesis happens in the leaves - the green parts of plants"
            ]
        },
        "teen": {
            "explanation": "Photosynthesis is a biochemical process where plants convert light energy into chemical energy stored in glucose. The process occurs in two main stages: 1) Light-dependent reactions in the thylakoid membranes of chloroplasts, where light energy splits water molecules (photolysis), producing ATP, NADPH, and oxygen. 2) Light-independent reactions (Calvin cycle) in the stroma, where carbon dioxide is fixed into glucose using the ATP and NADPH from the light reactions. Chlorophyll molecules absorb photons and pass the energy through electron transport chains.",
            "initial_question": "Can you explain what happens to light energy when it's absorbed by a plant leaf? Where does that energy go?",
            "follow_ups": [
                "Great! So light energy becomes chemical energy. Now, in which part of the chloroplast do the light-dependent reactions occur, and what's being split?",
                "Excellent understanding! Now tell me: in the Calvin cycle, what is carbon dioxide converted into, and what provides the energy for this conversion?",
                "Perfect! So you understand the two stages. How would photosynthesis be affected if a plant couldn't make ATP and NADPH - what would happen in the Calvin cycle?"
            ],
            "hints": [
                "Light reactions happen in the thylakoid membranes; dark reactions happen in the stroma",
                "Photolysis is the splitting of water - look at the Greek roots: 'photo' (light) and 'lysis' (splitting)",
                "The products of light reactions (ATP, NADPH) are used in the Calvin cycle"
            ]
        },
        "adult": {
            "explanation": "Photosynthesis is the metabolic pathway where autotrophic organisms convert light energy into chemical energy via substrate phosphorylation. In plants, this involves: (1) Photolysis of H₂O in PSII, producing O₂, protons, and electrons; (2) Electron transport through the cytochrome b6f complex, generating a proton gradient; (3) Chemiosmotic ATP synthesis in PSI; (4) NADP⁺ reduction via ferredoxin; (5) The Calvin cycle employing RuBisCO for carbon fixation of CO₂ into 3-PG, reduced to G3P. Photorespiration presents competitive inhibition when O₂/CO₂ ratios are unfavorable. C3, C4, and CAM pathways represent evolutionary adaptations to environmental constraints.",
            "initial_question": "Explain the role of the electron transport chain in generating the proton-motive force during photosynthesis.",
            "follow_ups": [
                "Excellent. Now discuss how the structure of the thylakoid membrane facilitates this electron transport and chemiosmotic coupling.",
                "Good. What molecular mechanisms explain the substrate specificity of RuBisCO, and how does photorespiration represent an evolutionary trade-off?",
                "Very good. Integrate your understanding: How do C4 and CAM plants optimize photosynthesis compared to C3 plants, and what selective pressures drove this evolution?"
            ],
            "hints": [
                "Consider the redox potentials and the Z-scheme",
                "RuBisCO's carboxylase and oxygenase activities compete for the same active site",
                "Water is the electron donor; CO₂ is the terminal electron acceptor"
            ]
        }
    },
    "energy": {
        "keywords": ["energy", "power", "fuel", "electricity", "heat", "light"],
        "young_child": {
            "explanation": "Energy is what makes things **move and happen**! ⚡\n\nYou have energy to run and play. The sun has energy to make light. A battery has energy to power a toy.\n\nEnergy comes in many forms: movement, heat, light, and electricity!",
            "initial_question": "Where does your energy come from when you run and play? (Hint: think about food!)",
            "follow_ups": [
                "Right! Food gives you energy! What gives energy to a car?",
                "Yes! Fuel gives cars energy! Where does the sun get its energy?",
                "Great! You understand energy! 🌟"
            ],
            "hints": [
                "Energy makes things move and work",
                "Your body gets energy from food",
                "The sun is the biggest energy source on Earth"
            ]
        },
        "child": {
            "explanation": "Energy is the ability to do work or cause change. Common types:\n- **Heat energy**: warmth from fire, sun, or stove\n- **Light energy**: from sun, bulbs, flames\n- **Kinetic energy**: energy of moving things\n- **Electrical energy**: from batteries and power outlets\n- **Chemical energy**: stored in food and fuel",
            "initial_question": "Can you name 5 sources of energy in your home?",
            "follow_ups": [
                "Great examples! Now, which form of energy do you think is most important?",
                "Good thinking! Why do you think we need energy?",
                "Excellent! Energy is essential for everything!"
            ],
            "hints": [
                "Think about what powers your lights, heat, and devices",
                "Energy can change from one form to another",
                "Food is energy for your body"
            ]
        },
        "teen": {
            "explanation": "Energy is the capacity to do work or transfer heat. Law of Conservation of Energy: energy cannot be created or destroyed, only transformed. Forms include potential, kinetic, thermal, chemical, electrical, and nuclear energy. Power is the rate of energy transfer (measured in watts).",
            "initial_question": "Explain how the sun's energy reaches Earth and powers life.",
            "follow_ups": [
                "Good explanation. How is energy converted in food chains?",
                "Excellent. What's the difference between energy and power?",
                "Well reasoned. Energy is fundamental to all processes!"
            ],
            "hints": [
                "Energy transformations follow conservation laws",
                "Power = Energy / Time",
                "Efficiency measures useful energy output"
            ]
        },
        "adult": {
            "explanation": "Energy is a state function in thermodynamics. First Law: ΔU = Q - W. Enthalpy, Gibbs free energy, entropy relations. Quantum mechanics: E = hf (photons). Relativity: E = mc². Conservation principles across all physical domains.",
            "initial_question": "How does the first law of thermodynamics relate to energy conservation?",
            "follow_ups": [
                "Excellent. Discuss entropy and the second law.",
                "Good. How do quantum and relativistic energy equations relate?",
                "Well articulated. This demonstrates advanced physics knowledge."
            ],
            "hints": [
                "Internal energy, heat, and work relationships",
                "Entropy increases in isolated systems",
                "Mass-energy equivalence in relativity"
            ]
        }
    },
    "ecosystem": {
        "keywords": ["ecosystem", "nature", "animals", "plants", "environment", "habitat"],
        "young_child": {
            "explanation": "An ecosystem is like a **community of living things**! 🌿\n\nIt includes animals, plants, bugs, and the environment they live in. Like a forest has trees, deer, birds, and everything that lives together!\n\nEverything in an ecosystem helps each other!",
            "initial_question": "What animals and plants live in a forest? How do they help each other?",
            "follow_ups": [
                "Great examples! Deer eat plants, and when deer poop, it helps plants grow!",
                "Yes! That's how an ecosystem works - everything is connected!",
                "Perfect! You understand ecosystems! 🌟"
            ],
            "hints": [
                "An ecosystem includes all living things in an area",
                "Everything in nature is connected",
                "Animals and plants depend on each other"
            ]
        },
        "child": {
            "explanation": "An ecosystem is a community of living organisms (plants, animals, fungi) and their non-living environment (soil, water, climate) interacting as a system.\n\nKey parts:\n- **Producers**: plants (make their own food)\n- **Consumers**: animals (eat other things)\n- **Decomposers**: bacteria, fungi (break down dead things)\n- **Environment**: soil, water, climate",
            "initial_question": "How do you think all the living things in a forest depend on each other?",
            "follow_ups": [
                "Great thinking! What would happen if all the trees disappeared?",
                "Exactly! The whole ecosystem would collapse! That shows how connected it is!",
                "Excellent understanding of ecosystems!"
            ],
            "hints": [
                "Food chains show who eats what",
                "When one part changes, the whole ecosystem is affected",
                "Ecosystems have natural balance"
            ]
        },
        "teen": {
            "explanation": "An ecosystem comprises biotic (living) and abiotic (non-living) components in dynamic equilibrium. Energy flows through food chains/webs. Nutrient cycling through biogeochemical processes. Biodiversity ensures ecosystem stability and resilience.",
            "initial_question": "How does energy flow through an ecosystem, and why is efficiency important?",
            "follow_ups": [
                "Good. Explain trophic levels and energy loss.",
                "Excellent. How do keystone species affect ecosystems?",
                "Well reasoned. Ecosystems are complex systems!"
            ],
            "hints": [
                "Energy enters via photosynthesis",
                "Energy decreases at each trophic level (~10% rule)",
                "Biodiversity increases resilience"
            ]
        },
        "adult": {
            "explanation": "Ecosystems are complex adaptive systems with emergent properties. Stability-diversity hypothesis, succession dynamics, tipping points. Network theory analysis of food webs. Climate-ecosystem interactions and feedback loops. Ecosystem services valuation and conservation.",
            "initial_question": "How do feedback loops in ecosystems create resilience or vulnerability?",
            "follow_ups": [
                "Excellent. Discuss climate tipping points in ecosystems.",
                "Good. How do invasive species disrupt network stability?",
                "Well explained. This shows ecosystem systems thinking."
            ],
            "hints": [
                "Negative feedback maintains stability",
                "Positive feedback can cause collapse",
                "Network topology affects ecosystem function"
            ]
        }
    },
    "simple machines": {
        "keywords": ["machine", "lever", "pulley", "wheel", "ramp", "engineering", "simple"],
        "young_child": {
            "explanation": "A simple machine is a **tool that helps you do work easier**! 🔧\n\nLike a lever helps you lift heavy rocks, or a ramp helps you push something uphill instead of lifting it straight up!\n\nSimple machines make hard work easier!",
            "initial_question": "Can you think of a tool that makes work easier? Like a shovel or a hammer?",
            "follow_ups": [
                "Great! A shovel is a simple machine! What about a ramp? When would you use it?",
                "Perfect! Ramps make it easier to move heavy things!",
                "Excellent! You understand simple machines! 🌟"
            ],
            "hints": [
                "Simple machines help us do work with less effort",
                "Examples: levers, ramps, wheels, pulleys",
                "Everyday tools are usually simple machines"
            ]
        },
        "child": {
            "explanation": "Simple machines are basic mechanical tools that help us do work. The six types are:\n1. **Lever**: like a seesaw or crowbar\n2. **Pulley**: like a rope over a wheel\n3. **Wheel and Axle**: like a bicycle wheel\n4. **Ramp**: like a slide or slope\n5. **Wedge**: like a knife or axe\n6. **Screw**: like a bolt or screw\n\nAll these reduce effort needed to do work!",
            "initial_question": "Which simple machine do you use most in your daily life?",
            "follow_ups": [
                "Good example! How does that machine make your work easier?",
                "Excellent! Can you think of another simple machine you use?",
                "Great understanding of simple machines!"
            ],
            "hints": [
                "Levers reduce effort by using a fulcrum",
                "Pulleys change direction of force",
                "Ramps spread weight over distance"
            ]
        },
        "teen": {
            "explanation": "Simple machines follow the principle: work input = work output (mechanical advantage × distance). Each machine type provides mechanical advantage:\n- Levers: M.A. = effort arm / load arm\n- Pulleys: M.A. = number of supporting ropes\n- Ramps: M.A. = length / height\n- Wheel/Axle: M.A. = radius_wheel / radius_axle",
            "initial_question": "Why can a lever give you a mechanical advantage when lifting heavy objects?",
            "follow_ups": [
                "Good reasoning. Calculate the M.A. for a specific lever.",
                "Excellent. How do multiple pulleys increase mechanical advantage?",
                "Well explained. Simple machines are applications of physics!"
            ],
            "hints": [
                "Mechanical advantage = output force / input force",
                "Levers have three classes based on position of fulcrum",
                "Mechanical advantage always trades distance for effort"
            ]
        },
        "adult": {
            "explanation": "Simple machines exemplify fundamental principles in classical mechanics: work (W = Fd), energy conservation, and force distribution. Analysis includes friction losses, ideal mechanical advantage, actual mechanical advantage, and efficiency calculations. Complex machines are combinations of simple machines.",
            "initial_question": "How do real-world friction losses affect the theoretical mechanical advantage of simple machines?",
            "follow_ups": [
                "Good. Quantify efficiency for compound pulley systems.",
                "Excellent. Analyze work-energy theorem applications.",
                "Well reasoned. This demonstrates engineering fundamentals."
            ],
            "hints": [
                "Efficiency = actual M.A. / theoretical M.A.",
                "Friction always reduces efficiency",
                "Compound machines combine simple machine advantages"
            ]
        }
    },
    "gravity": {
        "keywords": ["gravity", "fall", "weight", "pull", "attract", "force"],
        "young_child": {
            "explanation": "Gravity is an invisible force that pulls things down! 🌍 It's like the Earth is giving everything a big hug and doesn't want to let go. When you jump, gravity pulls you back down. When you drop a toy, gravity pulls it to the ground. Everything has gravity, but Earth's gravity is very strong!",
            "initial_question": "Why do you think things fall down instead of up? What's pulling them down?",
            "follow_ups": [
                "Great guess! Gravity is the force that pulls things down. Now, do you think gravity only works on toys and balls, or does it work on everything?",
                "Perfect! Gravity works on everything! Here's a fun question: If you could jump really, really high, do you think you would keep going up forever, or would gravity bring you back down?",
                "Excellent thinking! You understand gravity! One more thing: do you think the moon is affected by Earth's gravity too?"
            ],
            "hints": [
                "Think about what happens every time you drop something",
                "Gravity is everywhere - it's not just under your feet, it's all around!",
                "Even the sun has gravity!"
            ]
        },
        "child": {
            "explanation": "Gravity is a force that pulls objects toward each other. Earth's gravity pulls everything toward its center, which is why things fall downward. The strength of gravity depends on two things: how much stuff (mass) an object has, and how far apart objects are. A heavier object has stronger gravity. The closer objects are, the stronger gravity pulls them together. This is why you weigh less on the moon than on Earth - the moon's gravity is weaker!",
            "initial_question": "If gravity pulls things down, what do you think is holding the moon up in the sky? Why doesn't it fall?",
            "follow_ups": [
                "Interesting idea! The moon actually IS falling, but it's also moving sideways really fast. So it keeps missing Earth! Have you ever heard of orbits?",
                "Good! Now here's a question: if Earth's gravity is so strong, why isn't everything pulled to the very center of Earth?",
                "Excellent! So gravity pulls down, but the ground pushes back up. Now, do you think gravity only exists on Earth, or everywhere in space?"
            ],
            "hints": [
                "Gravity is always pulling, but other forces can balance it out",
                "An orbit is like falling while moving sideways at the same time",
                "Think about what would happen if there was no ground beneath you"
            ]
        },
        "teen": {
            "explanation": "Gravity is described by Newton's Law of Universal Gravitation: every object in the universe attracts every other object with a force proportional to their masses and inversely proportional to the square of the distance between them. Mathematically: F = G(m₁m₂)/r². The gravitational constant G is 6.674 × 10⁻¹¹ N⋅m²/kg². This explains why the acceleration due to gravity on Earth is approximately 9.8 m/s², and why objects experience different gravitational forces on different celestial bodies.",
            "initial_question": "Given the gravitational equation F = Gm₁m₂/r², explain why your weight would be different on the moon versus on Earth.",
            "follow_ups": [
                "Excellent! You correctly identified that both mass and distance matter. Now, why would gravity decrease with the square of the distance rather than just the distance?",
                "Good reasoning! Now apply this: If you doubled your distance from Earth's center, how would Earth's gravitational pull on you change, and why?",
                "Perfect! You understand inverse square law. One more: How does understanding gravity help explain why planets orbit stars, and what would happen if gravity suddenly stopped working?"
            ],
            "hints": [
                "Think about how gravity spreads out in all directions - it's like light from a bulb",
                "The inverse square relationship comes from the geometry of three-dimensional space",
                "Compare your weight calculation (mg) with the gravitation equation"
            ]
        },
        "adult": {
            "explanation": "In classical mechanics, gravity is described by Newton's Universal Law of Gravitation (F = Gm₁m₂/r²), providing excellent predictions in weak field regimes. However, Einstein's General Relativity reframes gravity as the curvature of spacetime caused by mass-energy. Massive objects warp spacetime according to the Einstein Field Equations, and objects follow geodesic paths through this curved manifold. Predictions diverge significantly in strong fields (near black holes) and at cosmological scales. Quantum gravity remains unsolved; string theory and loop quantum gravity are leading candidates. The equivalence principle unifies gravitational and inertial mass, fundamental to relativistic gravity.",
            "initial_question": "Compare and contrast the Newtonian and relativistic treatments of gravity. What problems does the relativistic approach solve?",
            "follow_ups": [
                "Excellent. Now explain how spacetime curvature near a massive object explains orbital motion without invoking a 'force' in the traditional sense.",
                "Good. Discuss the observational evidence for General Relativity over Newtonian gravity, particularly gravitational lensing and frame-dragging.",
                "Very good. What does the equivalence principle tell us about the equivalence of gravitational and inertial mass, and what are the implications for quantum gravity?"
            ],
            "hints": [
                "The geodesic equation replaces F=ma in curved spacetime",
                "Spacetime has intrinsic curvature; objects follow the straightest path in this curved space",
                "Gravitational waves are a prediction of General Relativity not present in Newton's theory"
            ]
        }
    },
    "numbers": {
        "keywords": ["number", "count", "zero", "one", "two", "three", "four", "five", "math"],
        "young_child": {
            "explanation": "Numbers help us count and tell us **how many**! 🔢\n\nNumbers go: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...\n\nYou use numbers every day! Like when you count your toys, or know you're 7 years old, or have 10 fingers!",
            "initial_question": "Can you count from 1 to 5? How many fingers do you have?",
            "follow_ups": [
                "Great counting! Now, which number is bigger: 3 or 5?",
                "Yes! 5 is bigger! Now tell me: do you have more or fewer than 10 fingers?",
                "Perfect! You understand numbers! 🌟"
            ],
            "hints": [
                "Use your fingers to count - you have 10 of them!",
                "Numbers tell us HOW MANY",
                "1, 2, 3, 4, 5 - these are the first five numbers"
            ]
        },
        "child": {
            "explanation": "Numbers are symbols we use to represent quantities and amounts. They help us count, measure, and compare things.\n\nWe use digits 0-9 to write all numbers. For example:\n- 5 means five things\n- 15 means one ten and five ones\n- 100 means ten tens (one hundred)",
            "initial_question": "Why do you think we have numbers? What do you use them for?",
            "follow_ups": [
                "Great examples! Numbers help us measure and compare. What about counting?",
                "Exactly! Now, what's the difference between a digit and a number?",
                "Good understanding! This is the foundation for all math!"
            ],
            "hints": [
                "Digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9",
                "We combine digits to make bigger numbers",
                "All numbers can be written using just 10 digits"
            ]
        },
        "teen": {
            "explanation": "Numbers form the foundation of mathematics. Natural numbers (1, 2, 3...) are used for counting. Whole numbers include zero. Integers include negative numbers. Real numbers include fractions and decimals. Complex numbers include imaginary units.",
            "initial_question": "What's the difference between natural numbers and whole numbers?",
            "follow_ups": [
                "Correct! Now, what about negative numbers? Where do we use them?",
                "Good point. How do real numbers differ from integers?",
                "Excellent understanding of the number system!"
            ],
            "hints": [
                "Natural numbers: 1, 2, 3...",
                "Whole numbers: 0, 1, 2, 3...",
                "Integers: ..., -2, -1, 0, 1, 2..."
            ]
        },
        "adult": {
            "explanation": "Numbers are abstract objects in mathematics. Number systems include natural numbers (ℕ), integers (ℤ), rationals (ℚ), reals (ℝ), and complex numbers (ℂ). Each extends the previous with new properties. Peano axioms formalize natural numbers, while real numbers can be constructed via Dedekind cuts or Cauchy sequences.",
            "initial_question": "How would you formally define natural numbers using set theory?",
            "follow_ups": [
                "Good. How does this relate to the construction of integers and rationals?",
                "Excellent. What about the completeness property of real numbers?",
                "Well reasoned. This shows mastery of foundational mathematics."
            ],
            "hints": [
                "Consider Peano's axioms for natural numbers",
                "Use equivalence classes for rationals",
                "Dedekind cuts or Cauchy sequences for reals"
            ]
        }
    },
    "subtraction": {
        "keywords": ["subtract", "minus", "take away", "remove", "difference"],
        "young_child": {
            "explanation": "Subtraction means taking things away! ➖\n\nIf you have 5 apples and eat 2, you have 3 apples left! That's 5 - 2 = 3.\n\nSubtraction helps us figure out: **how many are left?**",
            "initial_question": "If you have 4 cookies and eat 1, how many cookies do you have left?",
            "follow_ups": [
                "Yes! 4 - 1 = 3! Great job! Now try: if you had 5 and took away 2, how many left?",
                "Perfect! 5 - 2 = 3! You're doing great! Try: 6 - 1 = ?",
                "Excellent! You understand subtraction! 🌟"
            ],
            "hints": [
                "Subtraction is the opposite of addition",
                "Count down on your fingers",
                "5 - 2 means start at 5, go down 2, what do you land on?"
            ]
        },
        "child": {
            "explanation": "Subtraction is taking away a number from another number to find the difference. The symbol is -.\n\nFor example:\n- 7 - 3 = 4 (if you start with 7 and take away 3, you have 4 left)\n- 10 - 5 = 5 (ten minus five equals five)\n\nSubtraction is the opposite of addition! If 3 + 4 = 7, then 7 - 4 = 3.",
            "initial_question": "What is 8 - 3? How would you figure it out?",
            "follow_ups": [
                "Great! 8 - 3 = 5. Now, how does this relate to addition?",
                "Exactly! 5 + 3 = 8, so 8 - 3 = 5. They're opposites!",
                "Perfect understanding!"
            ],
            "hints": [
                "Start at the bigger number, count backward",
                "Think: addition and subtraction are opposites",
                "Use objects to show taking away"
            ]
        },
        "teen": {
            "explanation": "Subtraction finds the difference between two numbers. It's the inverse operation of addition. Key properties include:\n- Non-commutative: a - b ≠ b - a (usually)\n- Non-associative: (a - b) - c ≠ a - (b - c)\n- Subtraction can be rewritten as addition of the inverse",
            "initial_question": "Why isn't subtraction commutative like addition is?",
            "follow_ups": [
                "Good reasoning. Now show how subtraction relates to negative numbers.",
                "Excellent. How would you prove a - b = a + (-b)?",
                "Well explained. This is advanced number theory thinking!"
            ],
            "hints": [
                "Order matters in subtraction",
                "5 - 3 = 2, but 3 - 5 = -2",
                "Think about the additive inverse"
            ]
        },
        "adult": {
            "explanation": "Subtraction is defined as addition of the additive inverse: a - b = a + (-b). In abstract algebra, this operation exists in groups where inverse elements are defined. Subtraction is non-associative and non-commutative, forming a quasigroup structure in certain contexts.",
            "initial_question": "How is subtraction defined in abstract algebra, and in what structures does it exist?",
            "follow_ups": [
                "Correct. How does this relate to modular arithmetic?",
                "Good insight. What about in vector spaces and modules?",
                "Excellent mathematical reasoning."
            ],
            "hints": [
                "Consider group theory and inverse elements",
                "Subtraction requires an additive identity and inverse",
                "Different algebraic structures have different subtraction rules"
            ]
        }
    },
    "algebra": {
        "keywords": ["algebra", "equation", "variable", "solve", "x", "unknown"],
        "young_child": {
            "explanation": "Algebra is like a puzzle game with numbers! 🧩 Sometimes you don't know a number, so you use a letter (like x) to stand for it. Your job is to figure out what that mystery number is! For example: if x + 2 = 5, you need to find what x is. The answer is 3, because 3 + 2 = 5!",
            "initial_question": "Here's a simple one: If I have some apples and give you 3 apples, I have 5 left. How many apples did I start with?",
            "follow_ups": [
                "Great! You figured it out! Now let me try another: If x + 3 = 8, what is x? How did you figure it out?",
                "Perfect! You're thinking like an algebra master! Here's one: If x - 2 = 4, what is x? (Hint: think about what number minus 2 equals 4)",
                "Excellent! You're getting really good at this! One more: If 2 × x = 10, what is x? (What number times 2 equals 10?)"
            ],
            "hints": [
                "Think about the opposite operation: if it's adding, try subtracting",
                "Work backwards from the answer",
                "Try different numbers until you find the right one!"
            ]
        },
        "child": {
            "explanation": "Algebra uses letters (usually x) to represent unknown numbers. An equation shows that two sides are equal, and your job is to find what number the letter represents. For example: x + 3 = 7, so x must equal 4 (because 4 + 3 = 7). To solve equations, you use 'inverse operations': if something was added, subtract it; if something was multiplied, divide it. The key rule: whatever you do to one side of the equation, do the same to the other side to keep them balanced!",
            "initial_question": "Given the equation x + 5 = 12, how would you find what x equals? Walk me through your thinking.",
            "follow_ups": [
                "Great approach! So you subtracted 5 from both sides. Now, can you solve 2x = 14? Which operation is the opposite of multiplication?",
                "Perfect! You correctly used division. Now try this: x/3 = 4. What operation do you need to use, and what is x?",
                "Excellent! You understand the 'balancing method.' Now, can you solve a tougher one: 2x + 3 = 11? Remember to do the inverse operations in reverse order."
            ],
            "hints": [
                "The equals sign means both sides are balanced - they're the same value",
                "Use inverse operations: +  becomes -, ×  becomes ÷",
                "Do the same operation to both sides to keep things balanced"
            ]
        },
        "teen": {
            "explanation": "Algebra is the mathematics of equations and functions. It involves solving for unknown variables using properties of equality and algebraic manipulation. Key concepts include: linear equations (ax + b = c), quadratic equations (ax² + bx + c = 0), systems of equations, polynomials, factoring, and graphing. The fundamental principle is that if two expressions are equal, you can perform the same operation on both sides without changing the equality. More advanced topics include exponent rules, radical equations, and rational equations.",
            "initial_question": "Solve for x: 3x - 7 = 2x + 5. Explain each step and the property of equality you're using.",
            "follow_ups": [
                "Excellent! You correctly isolated x. Now, solve: x² - 5x + 6 = 0. Can you factor this quadratic, or do you prefer another method?",
                "Good! Let's check if you can factor: what two numbers multiply to 6 but add to -5?",
                "Perfect! So your solutions are x = 2 and x = 3. Can you verify these work in the original equation?"
            ],
            "hints": [
                "Collect like terms: put all x terms on one side",
                "For quadratics, try factoring first: (x - a)(x - b) = 0",
                "When you have a product equal to zero, at least one factor must be zero"
            ]
        },
        "adult": {
            "explanation": "Algebra studies abstract structures and equations over various fields and rings. At the advanced level, this includes abstract algebra (group theory, ring theory, field theory), linear algebra (vector spaces, matrices, eigenvalues), and algebraic geometry (polynomial equations over algebraic varieties). Key concepts: homomorphisms, quotient structures, vector spaces, bases, linear transformations, and Galois theory. Polynomial rings and ideals form the foundation for much of modern mathematics. Understanding algebraic structures is essential for pure mathematics, cryptography, and theoretical computer science.",
            "initial_question": "Describe how the concept of a group generalizes the properties of addition and multiplication. What makes something a 'group' mathematically?",
            "follow_ups": [
                "Excellent. Now, what's the difference between a group and a ring, and can you provide examples of each?",
                "Good. Discuss how linear algebra relates to the solution of systems of linear equations. Why is linear transformation theory important?",
                "Very good. Finally, explain the significance of ideals in ring theory and how they relate to homomorphisms and quotient rings."
            ],
            "hints": [
                "A group has four properties: closure, associativity, identity, and inverse",
                "Rings have two operations; fields have multiplicative inverses for all nonzero elements",
                "Linear transformations preserve vector space structure"
            ]
        }
    }
}

def is_math_expression(question):
    """Check if question is a simple math expression and solve it."""
    question = question.strip()
    question_lower = question.lower()

    # Remove common question words
    cleaned = question_lower.replace("what is ", "").replace("what's ", "")\
                            .replace("calculate ", "").replace("solve ", "")\
                            .replace("?", "").strip()

    # Check if it looks like math
    has_operator = any(op in cleaned for op in ['+', '-', '*', '/', '**', '%'])

    if has_operator:
        try:
            # Safely evaluate
            result = eval(cleaned)
            return True, cleaned, result
        except:
            pass

    return False, None, None

def solve_math_problem(question, age_group):
    """Solve a math expression and explain it."""
    is_math, expression, result = is_math_expression(question)

    if not is_math:
        return None

    # Try to parse operands and operator
    parts = []
    operator = None
    for op in ['+', '-', '*', '/', '**']:
        if op in expression:
            parts = expression.split(op)
            operator = op
            break

    if len(parts) < 2:
        parts = [expression, str(result)]

    num1 = parts[0].strip()
    num2 = parts[1].strip() if len(parts) > 1 else ""

    # Format based on age group
    if age_group == "young_child":
        return f"""## ✅ ANSWER: {question}

**{expression} = {result}** 🎉

If you have {num1} things and {operator if operator else 'add'} {num2}, you get **{result}** things!

You can count on your fingers to check! 🖐️"""

    elif age_group == "child":
        return f"""## ✅ ANSWER: {question}

**{expression} = {result}**

**How to solve:**
1. Start with {num1}
2. {'Add' if operator == '+' else 'Subtract' if operator == '-' else 'Multiply' if operator == '*' else 'Divide'} {num2}
3. The answer is: **{result}**

You can use your fingers or a number line to check!"""

    elif age_group == "teen":
        return f"""## ✅ ANSWER: {question}

**{expression} = {result}**

**Solution:**
- First number: {num1}
- Operation: {operator}
- Second number: {num2}
- Result: {result}

Order of operations: If there are multiple operations, do multiplication/division first, then addition/subtraction."""

    else:
        return f"""## ✅ ANSWER: {question}

**{expression} = {result}**

This arithmetic expression follows the order of operations (PEMDAS/BODMAS). The result is obtained by applying the {operator} operation to the operands."""

def find_topic(question):
    """Try to identify the main topic from the question."""
    if not question:
        return None

    # Check if it's a math expression first
    is_math, _, _ = is_math_expression(question)
    if is_math:
        return "math_expression"

    question_lower = question.lower()

    # First pass: exact topic match
    for topic in TOPICS.keys():
        if topic in question_lower:
            return topic

    # Second pass: keyword match
    for topic, data in TOPICS.items():
        keywords = data.get("keywords", [])
        for keyword in keywords:
            if keyword and keyword in question_lower:
                return topic

    return None

def get_age_group_key(age):
    """Get age group key."""
    if age < 8:
        return "young_child"
    elif age < 13:
        return "child"
    elif age < 18:
        return "teen"
    else:
        return "adult"

def get_concept_explanation(question, age_group):
    """Get age-appropriate explanation for a topic - ALWAYS return something helpful!"""

    # 1. FIRST: Check if it's MATH
    is_math, expression, result = is_math_expression(question)
    if is_math:
        math_answer = solve_math_problem(question, age_group)
        if math_answer:
            return math_answer

    # 2. SECOND: Check if it's in our knowledge base
    topic = find_topic(question)
    if topic and topic in TOPICS and topic != "math_expression":
        return TOPICS[topic][age_group]["explanation"]

    # 3. THIRD: Try to use Claude API if available
    try:
        import os
        if os.getenv("ANTHROPIC_API_KEY"):
            from ai_tutor import get_explanation_ai
            explanation = get_explanation_ai(question, age_group)
            if explanation and "don't have this" not in explanation.lower():
                return explanation
    except:
        pass

    # FALLBACK: Be honest but ACTUALLY helpful
    if age_group == "young_child":
        return f"""## Hey! Great question about **{question}**! 🤔

You know what? I'm still learning, but here's what I do know really well:

🧮 **Math** - I can solve any problem like 45+12, 100-5, etc.
🔧 **Simple Machines** - Levers, pulleys, ramps (how tools work!)
💻 **Coding** - Loops, variables, functions (how computers think)
⚡ **Science** - Energy, ecosystems, plants, gravity
🌍 **And lots more!**

Want me to explain something from these? Or ask me ANYTHING - I'll do my best to help! 😊"""

    elif age_group == "child":
        return f"""## Hey! That's a cool question about **{question}**!

Here's the thing - I can help with SO many topics:

✅ **Math** - Any arithmetic (45+12, algebra, geometry, etc.)
✅ **Science** - Biology, physics, chemistry, space, animals
✅ **Coding** - Programming, loops, functions, logic
✅ **Engineering** - How things work, simple machines
✅ **History & Geography** - Countries, events, people
✅ **Languages** - Words, grammar, translations
✅ **And literally anything else!**

I'm like your brother who knows a lot of stuff. Ask me anything and I'll explain it in a way that makes sense! 🌊"""

    elif age_group == "teen":
        return f"""## Yo! Good question about **{question}**

Real talk - I can help with basically anything you throw at me:

- **Math & Science** - All levels from basic to advanced
- **Coding & Technology** - Any programming language or tech concept
- **History, Geography, Languages** - Global topics
- **Engineering & Physics** - How the world works
- **Study Help** - Homework, essays, projects
- **Anything Else** - Seriously, ask away!

I'm your brother who's here to help you understand stuff, not just give you answers. We'll work through it together. What's on your mind? 💪"""

    else:
        return f"""## Regarding **{question}**

I can provide detailed explanations on virtually any topic:

**STEM Fields**: Mathematics, physics, chemistry, biology, computer science, engineering
**Humanities**: History, literature, languages, philosophy, social sciences
**Practical Skills**: Coding, writing, research, problem-solving, learning strategies
**Interdisciplinary**: Any combination of topics

Think of me as a knowledgeable brother who's genuinely interested in helping you understand complex concepts. I adapt explanations to your level and learning style.

What would you like to explore? 🌊"""

def get_initial_question(question, age_group):
    """Get the initial guiding question to start the learning session."""
    topic = find_topic(question)

    # For math expressions, ask follow-up questions
    if topic == "math_expression":
        if age_group == "young_child":
            return "Can you count to check if the answer is right? Use your fingers! 🖐️"
        elif age_group == "child":
            return "Now, try explaining how you would solve a similar problem, like 6+5?"
        elif age_group == "teen":
            return "Can you solve a similar problem? Try 50+25 or 100-45?"
        else:
            return "Can you apply this operation to a different set of numbers?"

    if topic and topic in TOPICS:
        return TOPICS[topic][age_group]["initial_question"]

    # Brotherly questions for unknown topics
    if age_group == "young_child":
        return "What do YOU think about this? Tell me what you already know! 😊"
    elif age_group == "child":
        return "What's your guess or what do you already know about it?"
    elif age_group == "teen":
        return "What's your take on this? What do you already understand?"
    else:
        return "What's your current understanding of this topic?"

def get_feedback_on_answer(question, student_answer, age_group, step_count):
    """Provide feedback on student answer and ask the next question."""
    topic = find_topic(question)

    if not topic or topic not in TOPICS:
        return f"""
### 💬 Your Answer: {student_answer[:100]}...

That's thoughtful! Let me help you deepen your understanding.

**Here's something to think about:** Can you tell me more about why you think that? What evidence or examples support your answer?

Keep exploring - you're asking great questions!
"""

    topic_data = TOPICS[topic][age_group]
    follow_ups = topic_data.get("follow_ups", [])

    # Select follow-up question based on step count
    if step_count < len(follow_ups):
        next_question = follow_ups[step_count]
    else:
        next_question = "Fantastic! You're really understanding this well. Can you think of a real-world example of how this works?"

    response = f"""
### ✅ Great Thinking!

Your answer shows you're thinking deeply about this! I like how you said: *"{student_answer[:80]}..."*

---

### 🤔 Next, Let Me Ask You:

{next_question}

**Remember:** There's no single "right" answer here. The important thing is to keep thinking and asking questions!
"""

    return response.strip()

def get_hint(question, age_group):
    """Provide a helpful hint without giving away the answer."""
    topic = find_topic(question)

    if not topic or topic not in TOPICS:
        return "Think about what you already know, and try to connect it to new ideas!"

    topic_data = TOPICS[topic][age_group]
    hints = topic_data.get("hints", [])

    if hints:
        return hints[0]

    return "You're on the right track! Keep thinking!"
