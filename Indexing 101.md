# Indexing 101

## Indexing on <u>one</u> axis:

Use the index operator **[ : ]** directly on a DataFrame

- to select **columns** use
    - a single column name: `df[ 'A' ]` -> Series
    - a list of column names: `df[ ['A', 'B'] ]` -> DataFrame


- to select **rows** use
    - a slice object: `df[start:stop:step]`
    - a boolean array: `df[ df['A'] > 0 ]`
    - a partial time string: `df[ '2019-09' ]`

**Chained indexing** is possible like with `df[ 'A' ][ 2: ]`, but should be used for lookups only - not for assignments. Don't ignore the SettingWithCopy warning!

## Simultaneous indexing on <u>two</u> axis:

- via label: **`.loc[ :, : ]`** with
    - a string
    - a list of strings
    - a slice notation using strings as the start and stop values
    - a boolean array
    - a partial time string


- via position: **`.iloc[ :, : ]`** with
    - an integer
    - a list of integers
    - slice notation with ints as the start and stop values
    - a boolean array
 

When indexing on the column axis only, use an empty slice `[ : ]` as the first argument, e.g. `df.loc[ :, 'A':'C' ]`

 

Attributes **.at** and **.iat** are for scalars only and rarely needed.

Attribute **.ix** is deprecated.