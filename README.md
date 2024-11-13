# Alliteration Finder in Persian Poems

This Python script is designed to analyze Persian poems and identify alliterative words (words that start with the same consonant sound). It can be used to find the most frequent consonant sounds in each line of a poem and the words that contain those sounds.

## Features
- Identifies the most frequent consonant sounds in each line of a poem
- Provides the normalized frequency of each frequent consonant sound
- Lists the words that contain each frequent consonant sound
- Writes the results to an output file for further analysis

## Usage
1. Ensure you have Python 3.x installed on your system.
2. Save the poem text in a file (e.g., `data.txt`) in the same directory as the script.
3. Run the script using the following command:

   ```
   python alliteration_finder.py
   ```

   This will generate an output file named `consonance_output.txt` in the same directory, containing the alliteration analysis for each line of the poem.

4. Adjust the `threshold` parameter in the `find_consonance_per_line()` function to control the minimum normalized frequency required for a consonant to be considered "frequent". The default value is 0.1 (10%).

## Example Output
```
Line 1:
Consonant: 'خ', Normalized Value: 0.13
Words containing this consonant: خیزید, خز, خزان

Line 2:
Consonant: 'ب', Normalized Value: 0.12
Words containing this consonant: باد, بجانب
Consonant: 'و', Normalized Value: 0.10
Words containing this consonant: وزان
```

## Limitations
- The script currently only works with Persian poems, as it uses a predefined list of Persian consonants.
- The script does not handle diacritics or vowel sounds, which can also contribute to alliteration in Persian poetry.
- The script does not provide any visualization or advanced analysis of the alliterative patterns in the poem.

## Contributing
If you have any suggestions for improving this script or would like to extend its functionality, feel free to submit a pull request or open an issue on the repository.
