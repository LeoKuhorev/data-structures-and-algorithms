"use strict";

/* ------------------------------------------------------------------------------------------------
CHALLENGE 1

Write a function named getCourseKeys that takes in the courseInfo object and returns an array containing the keys for the courseInfo object.

For example: (['name', 'duration', 'topics', 'finalExam']).
------------------------------------------------------------------------------------------------ */
const courseInfo = {
  name: "Code 301",
  duration: { dayTrack: "4 weeks", eveningTrack: "8 weeks" },
  topics: [
    "SMACSS",
    "APIs",
    "NodeJS",
    "SQL",
    "jQuery",
    "functional programming",
  ],
  finalExam: true,
};

const getCourseKeys = (obj) => Object.keys(obj);

/* ------------------------------------------------------------------------------------------------
CHALLENGE 2
Use the characters data below for the remainder of the challenges.

Write a function named getHouses that returns a new array containing the names of all of the houses in the data set.
------------------------------------------------------------------------------------------------ */

let characters = [
  {
    name: "Eddard",
    spouse: "Catelyn",
    children: ["Robb", "Sansa", "Arya", "Bran", "Rickon"],
    house: "Stark",
  },
  {
    name: "Jon A.",
    spouse: "Lysa",
    children: ["Robin"],
    house: "Arryn",
  },
  {
    name: "Cersei",
    spouse: "Robert",
    children: ["Joffrey", "Myrcella", "Tommen"],
    house: "Lannister",
  },
  {
    name: "Daenarys",
    spouse: "Khal Drogo",
    children: ["Drogon", "Rhaegal", "Viserion"],
    house: "Targaryen",
  },
  {
    name: "Mace",
    spouse: "Alerie",
    children: ["Margaery", "Loras"],
    house: "Tyrell",
  },
  {
    name: "Euron",
    spouse: null,
    children: [],
    house: "Greyjoy",
  },
  {
    name: "Jon S.",
    spouse: null,
    children: [],
    house: "Snow",
  },
];

const getHouses = (arr) => arr.map(({ house }) => house);

/*------------------------------------------------------------------------------------------------
CHALLENGE 3

Write a function named hasChildrenValues that uses Object.values to determine if any given character in the data set has children.

This function should take in an array of data and a character name and return a Boolean.

For example:
hasChildrenValues(characters, 'Cersei') will return true
hasChildrenValues(characters, 'Sansa') will return false
------------------------------------------------------------------------------------------------ */

const hasChildrenValues = (arr, character) => {
  let children = false;
  arr.forEach((element) => {
    if (Object.values(element)[0] === character) {
      if (Object.values(element)[2].length > 0) {
        children = true;
      }
    }
  });
  return children;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 4

Write a function named hasChildrenEntries that is similar to your hasChildrenValues function from challenge 3, but uses the data's entries instead of its values.

The input and output of this function are the same as the input and output from challenge 3.
------------------------------------------------------------------------------------------------ */

const hasChildrenEntries = (arr, character) => {
  let children = false;
  arr.forEach((element) => {
    if (Object.entries(element)[0][1] === character) {
      if (Object.entries(element)[2][1].length > 0) {
        children = true;
      }
    }
  });
  return children;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 5

Write a function named totalCharacters that takes in an array and returns the number of characters in the array.
------------------------------------------------------------------------------------------------ */

const totalCharacters = (arr) => {
  let characters = 0;
  arr.forEach((element) => {
    let house = Object.values(element);
    for (let i = 0; i < house.length - 1; i++) {
      if (house[i]) {
        Array.isArray(house[i])
          ? (characters += house[i].length)
          : (characters += 1);
      }
    }
  });
  return characters;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 6 - Stretch Goal

Write a function named houseSize that takes in the array of characters and creates an object for each house containing the name of the house and the number of members.

All of these objects should be added to an array named "sizes". Return the "sizes" array from the function.

For example: [{ house: 'Stark', members: 7 }, { house: 'Arryn', members: 3 }, ... ].
------------------------------------------------------------------------------------------------ */

const houseSize = (arr) => {
  const sizes = [];

  arr.forEach((element) => {
    let count = 0;
    Object.keys(element).forEach((property) => {
      if (property !== "house" && element[property]) {
        Array.isArray(element[property])
          ? (count += element[property].length)
          : (count += 1);
      }
    });
    sizes.push({ house: element.house, members: count });
  });

  return sizes;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 7 - Stretch Goal

As fans are well aware, "When you play the game of thrones, you win or you die. There is no middle ground."

We will assume that Alerie Tyrell is deceased. She missed her daughter's wedding. Twice.

Write a function named houseSurvivors. You may modify your houseSize function from challenge 6 to use as the basis of this function.

This function should create an object for each house containing the name of the house and the number of members. If the spouse is deceased, do not include him/her in the total number of family members.

All of these objects should be added to an array named "survivors". Return the "survivors" array from the function.

For example: [ { house: 'Stark', members: 6 }, { house: 'Arryn', members: 2 }, ... ].
------------------------------------------------------------------------------------------------ */

const deceasedSpouses = ["Catelyn", "Lysa", "Robert", "Khal Drogo", "Alerie"];

const houseSurvivors = (arr) => {
  const survivors = [];

  arr.forEach((element) => {
    let members = [];
    Object.keys(element).forEach((property) => {
      if (property !== "house" && element[property]) {
        Array.isArray(element[property])
          ? members.push(...element[property])
          : members.push(element[property]);
      }
    });

    for (let i in members) {
      for (let k in deceasedSpouses) {
        if (members[i] === deceasedSpouses[k]) {
          members.splice(i, 1);
        }
      }
    }

    survivors.push({ house: element.house, members: members.length });
  });

  return survivors;
};

/* ------------------------------------------------------------------------------------------------
TESTS

All the code below will verify that your functions are working to solve the challenges.

DO NOT CHANGE any of the below code.

Run your tests from the console: jest challenges-06.test.js

------------------------------------------------------------------------------------------------ */

describe("Testing challenge 1", () => {
  test("It should return the keys from an object", () => {
    expect(getCourseKeys(courseInfo)).toStrictEqual([
      "name",
      "duration",
      "topics",
      "finalExam",
    ]);
  });
});

describe("Testing challenge 2", () => {
  test("It should return an array of the names of the houses", () => {
    expect(getHouses(characters)).toStrictEqual([
      "Stark",
      "Arryn",
      "Lannister",
      "Targaryen",
      "Tyrell",
      "Greyjoy",
      "Snow",
    ]);
    expect(getHouses(characters).length).toStrictEqual(7);
  });
});

describe("Testing challenge 3", () => {
  test("It should return true for characters that have children", () => {
    expect(hasChildrenValues(characters, "Daenarys")).toBeTruthy();
  });

  test("It should return false to characters who do not have children", () => {
    expect(hasChildrenValues(characters, "Sansa")).toBeFalsy();
  });
});

describe("Testing challenge 4", () => {
  test("It should return true for characters that have children", () => {
    expect(hasChildrenEntries(characters, "Eddard")).toBeTruthy();
  });

  test("It should return false to characters who do not have children", () => {
    expect(hasChildrenEntries(characters, "Jon S.")).toBeFalsy();
  });
});

describe("Testing challenge 5", () => {
  test("It should return the number of characters in the array", () => {
    expect(totalCharacters(characters)).toStrictEqual(26);
  });
});

describe("Testing challenge 6", () => {
  test("It should return an object for each house containing the name and size", () => {
    expect(houseSize(characters)).toStrictEqual([
      { house: "Stark", members: 7 },
      { house: "Arryn", members: 3 },
      { house: "Lannister", members: 5 },
      { house: "Targaryen", members: 5 },
      { house: "Tyrell", members: 4 },
      { house: "Greyjoy", members: 1 },
      { house: "Snow", members: 1 },
    ]);
    expect(houseSize(characters).length).toStrictEqual(7);
  });
});

describe("Testing challenge 7", () => {
  test("It should not include any deceased spouses", () => {
    expect(houseSurvivors(characters)).toStrictEqual([
      { house: "Stark", members: 6 },
      { house: "Arryn", members: 2 },
      { house: "Lannister", members: 4 },
      { house: "Targaryen", members: 4 },
      { house: "Tyrell", members: 3 },
      { house: "Greyjoy", members: 1 },
      { house: "Snow", members: 1 },
    ]);
  });
});
