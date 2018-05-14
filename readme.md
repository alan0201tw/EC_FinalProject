演化計算Todo
---
# Text EA System

- 根據 Proposal 裡面的 spec 實作。
- 應包含兩個 class : World , Chromesome. 範例可以參考[裡面](https://github.com/alan0201tw/CSharp_EC_CourseAssignment/tree/master/HW1_Simulation/HW1_Simulation)的 World , Creature

## World
1. Constructor ( and initialization )
2. Maintain Best Fitness Chromesome ( update every time the world goes to next generation )
3. ToNextGeneration(SelectionType selectionType)
4. ParentSelection(out int parentIndex1, out int parentIndex2, SelectionType selectionType) 
   // selection type can be arbitrary

## Chromesome
1. Override ToString function ( or just have a function to represent the individual in string form )
2. CompareTo function (To decide parent)
3. Constructors ( no parameter for initialization , and one with two chromesome as 2 parents )
4. GetFitness function ( for performance, this can be update only when data is changed )

* Representations ( in pseudo code and abstract concept ) :

```
Chromesome = ( Sentence )*
Sentence = (phrase) (connections + phrase)* (terminations);

struct Chromesome
{
    List <Sentence> Sentences;
}

struct Sentence
{
    Phrase startingPhrase;
    List < FollowUpPhrase > followUpPhrases;
    int terminationIndex; // this index represents a single termination in text file.
}

struct Phrase 
{
    int subjectiveIndex;
    int verbIndex;
    int objectiveIndex; // -1 for no objectives
}

struct FollowUpPhrase
{
    int connectionIndex;

    int subjectiveIndex;
    int verbIndex;
    int objectiveIndex; // -1 for no objectives
}
```
- 某些 function 會用到使用者設定的文庫檔，所以要寫好維護這些單詞的 manager 並提供全域、簡潔的 api。
- 下方的 Judge 系統要跟著這個 manager，就可以不用讀文字，而是讀個體的representation就好。

# Simple Judge System
- 使用者設定 text file 時不會另外指定單字的情緒，但我們在開發時可以這樣做。
- 然後一個句子的情緒值可以用 : verb.value() * object.value() 來決定。

- 例如我的動詞庫以及受詞庫分別長這樣...

| verb | score | noun | score |
|------|-------|------|-------|
|like | 0.7 | apple | 0.3 |
|love | 0.9 | hero  | 0.8 |
|hate |-0.9 | alcohol | -0.3 |
|dislike |-0.7 |demon| -0.8 |

- 然後今天這個系統收到了一個句子...
```
I like demon. -> 系統會 return 0.7 * -0.8 = -0.56
I love hero. -> 0.9 * 0.8 = 0.72
```
- 利用這樣簡單的 single value 來評定我們的句子是否有真的向我們訂出的目標演化。
- 如果沒有，就修正演算法，直到在這個Judge System中成功演化，才使用第三方的情緒分析。
- 這個用意是減少api的使用次數。

# 備註
- 終止條件
    1. world過幾代
    2. finess < threshold
- 數字：5 X 10 X 10(S. + V. + O.)
- connection: and/,
- chrmosome>sentence>phrase
- sentence的分數是用phrase的平均
- chrmosome是很多個sentence的平均
- 分數： v(v, o)
