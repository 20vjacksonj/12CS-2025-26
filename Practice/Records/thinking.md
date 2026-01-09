# Spotify Music Library Problem - Solution Analysis

**Aim:** Create a program that simulates a Spotify-style music library using a 2D array to store song records in an object called SONGS.

**Process:** Each record should be built from user inputs containing:
- Song name
- Artist name
- Number of likes
- Favourite status (boolean)

---

## Understanding the Data Structure

### Why 2D Arrays?

A **2D array** (array of arrays) is ideal for this problem because:

1. **Rows represent individual songs** - Each row is one complete song record
2. **Columns represent song attributes** - Each column holds a specific piece of information (name, artist, likes, favourite)
3. **Easy iteration** - We can loop through rows to process all songs
4. **Consistent structure** - Every song has the same data fields in the same order

### Visual Representation

```
SONGS = [
    ["Song Name 1", "Artist 1", 1500, True],
    ["Song Name 2", "Artist 2", 850, False],
    ["Song Name 3", "Artist 3", 2300, True]
]
```

Each inner array represents ONE song with its four attributes.

---


## Programming Considerations

### 1. **Loop for Multiple Entries**

Users will want to add multiple songs, so we need a loop:

```python
while True:
    # Collect input
    # Create record
    # Add to SONGS
    
    continue_adding = input("Add another song? (yes/no): ")
    if continue_adding.lower() != "yes":
        break
```

### 2. **Input Validation**

Good practice includes checking for:
- Empty strings for song/artist names
- Negative numbers for likes
- Valid yes/no responses for favourite status

### 3. **Accessing Data Later**

To retrieve specific information:

```python
# Get all song names
for song in SONGS:
    print(song[0])  # Index 0 is song name

# Get favourite songs only
for song in SONGS:
    if song[3]:  # Index 3 is favourite status
        print(f"{song[0]} by {song[1]}")
```

### 4. **Data Persistence**

Consider:
- How to save SONGS to a file for future sessions
- How to load previously saved data
- File formats (JSON, CSV, pickle)

---

## Alternative Approaches (For Comparison)

### Using Dictionaries (More Pythonic)

```python
SONGS = [
    {"name": "Song 1", "artist": "Artist 1", "likes": 1500, "favourite": True},
    {"name": "Song 2", "artist": "Artist 2", "likes": 850, "favourite": False}
]
```

**Advantages:**
- Self-documenting (keys show what each value represents)
- No need to remember index positions
- Can add/remove fields easily

**Disadvantages:**
- Slightly more memory overhead
- More verbose
### Using a Class (Object-Oriented Approach)


**Advantages:**
- Can add methods (e.g., `song.display()`, `song.like()`)
- Type hints and IDE support
- Encapsulation of related data and behaviour

---

## Potential Extensions

Once the basic structure works, consider adding:

1. **Search functionality** - Find songs by name or artist
2. **Sorting** - Order by likes, alphabetically, or favourites first
3. **Statistics** - Total likes, most popular artist, percentage of favourites
4. **Edit/Delete** - Modify or remove existing records
5. **Display formatting** - Pretty print the library in a table format
6. **Import from file** - Load a pre-made collection
7. **Playlist creation** - Group songs into themed collections

---

## Key Learning Outcomes

This problem teaches:

✓ **2D array manipulation** - Creating, populating, and accessing nested arrays  
✓ **Data type handling** - Converting strings to integers and booleans  
✓ **User input processing** - Gathering and validating keyboard input  
✓ **Loop control** - Using while loops for repeated data entry  
✓ **Data modelling** - Representing real-world entities in code  
✓ **Index-based access** - Understanding how to retrieve specific elements

---

## Common Pitfalls to Avoid

⚠️ **Inconsistent ordering** - Always add attributes in the same order  
⚠️ **Type mismatches** - Remember to convert likes to int, favourite to bool  
⚠️ **Index errors** - Check array bounds before accessing elements  
⚠️ **Empty inputs** - Validate that users actually enter data  
⚠️ **Magic numbers** - Consider using constants for index positions

---

## Summary

The Spotify library problem is an excellent introduction to working with **structured data** in arrays. By using a 2D array where each row represents a song and each column represents an attribute, we can efficiently store and manipulate collections of related information. This mirrors how real databases and music streaming services organize their data, making it both educationally valuable and practically relevant.

The key is maintaining **consistency** in how records are structured and being mindful of **data types** when processing user input.




## My Notes
* Record - a collection of related information thats well organised
* Records have mulitple fields
* Implement a record in python:
    * 