# Rick and Morty Story Bot

Hey there, interdimensional traveler, welcome to my *Rick and Morty* bot. This little beauty uses **OpenAI's GPT-4**  to spit out answers as yours truly—Rick Sanchez. It also hooks into **[The Rick and Morty API](https://rickandmortyapi.com/)** to fetch info on your favorite characters in the show. Wanna find out where Mr. Poopybutthole’s been? Boom, I got you covered.



### Features 

- Responds as *me*, Rick Sanchez (the one and only).
- Fetches character info like status (alive or dead...), species, gender, and what episodes they’re in.
- Handles errors better than Morty handles life.
- Integrates with OpenAI's GPT-4 model for generating responses.



### Prerequisites

1. Python 3.7 or later.
2. A valid API key for OpenAI (Azure setup).
3. Required Python packages installed:
   - `openai`
   - `requests`

```
pip install openai requests
```



### Setting It Up (Even Jerry can do this... maybe)

#### Step 1: Set Your Keys Ready

Set your **Azure API Key** and **Endpoint** as environment variables:

```
set AZURE_KEY=your_api_key_here
set AZURE_ENDPOINT=your_azure_endpoint_here
```

(You need to re-set these everytime when you restart the terminal)

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### Step 3: Read the Code (Or Don’t, Whatever)

- **`charater_live`**: This function talks to the Rick and Morty API and gets juicy details about your chosen character, which includes:
  - character_episode
  - character_status
  - character_species
  - character_gender
- **`functions` List**: This tells GPT-4 how to call `charater_live`. 
- **Main Bot Logic**: GPT-4 decides when to fetch data and when to, you know, just improvise like me after a few drinks.



### Running the Bot

#### Step 1: Start the Thing

```
python RickandMorty_bot.py
```

### Step 2: Ask Questions

Example:

```
Find Rick Sanchez and his episodes in Rick and Morty
```

The output will be:

```
plaintextCopy codeRick Sanchez appears in the episodes: https://rickandmortyapi.com/api/episode/1, https://rickandmortyapi.com/api/episode/2.
Gender: Male
Species: Human
Status: Alive
```

Boom. Science.



### Example Output 

#### Input:

```
Find Baby Poopybutthole and his story in Rick and Morty
```

#### Output:

```
plaintextCopy codeBaby Poopybutthole appears in the episodes: https://rickandmortyapi.com/api/episode/10.
Gender: Male
Species: Humanoid
Status: Alive
```

#### Bot's Output:

It could be...

```
"Geez, you're really scraping the bottom of the barrel here, aren't you? Alright, alright, fine, I'll help you out. Baby Poopybutthole is, uh, well... you remember Mr. Poopybutthole, right? He's that... well, you know. Anyways, Baby Poopybutthole is a similar character and he's even more of a mystery. We see him grow up in the end credit sequence of "The Poop in My Pants" but most of his "story" is just mundane life stuff, birthdays, funerals, snake bites, the usual. Isn't that just riveting? Poopybutthole lore, the real pulse-pounding science fiction you tune in for. Alright, I'm done. Anyone else have any...less stupid questions?""
```

(You’re welcome, by the way.)



### References

- [Rick and Morty API](https://rickandmortyapi.com/) - Because I’m not pulling this info out of thin air.
- [OpenAI API Docs](https://platform.openai.com/docs) - The GPT-4 brain I occasionally borrow.



### Final Thoughts 

If this bot breaks reality, it’s on you. If it works, thank me by naming an interdimensional invention after me. Now go run the bot and stop wasting my time, Morty!