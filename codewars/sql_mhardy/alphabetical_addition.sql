-- Your task is to add up letters to one letter.

-- In SQL, you will be given a table letters, with a string column letter. Return the sum of the letters in a column letter.

-- Notes:
-- Letters will always be lowercase.
-- Letters can overflow (see second to last example of the description)
-- If no letters are given, the function should return 'z'
-- Examples:
-- table(letter: ["a", "b", "c"]) = "f"
-- table(letter: ["a", "b"]) = "c"
-- table(letter: ["z"]) = "z"
-- table(letter: ["z", "a"]) = "a"
-- table(letter: ["y", "c", "b"]) = "d" -- notice the letters overflowing
-- table(letter: []) = "z"

-- # write your statement here, see description for setup.

SELECT COALESCE(CHR(CAST((SUM(ascii(letter) - 96) -1) % 26 AS int)+97), 'z') AS letter
FROM letters;