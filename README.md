# Karel Helper Functions

## Overview

im too lazy to write an actual readme so i had chatgpt do it for me, its accurate though

This is a small collection of helper functions designed to make **CodeHS Karel assignments** easier to write.

Instead of repeatedly writing the same Karel command multiple times, these functions allow you to perform an action a specific number of times with a single command.

For example, instead of:

```python
move()
move()
move()
```

You can write:

```python
f_move(3)
```

These functions are meant to **assist with repetitive actions**. They do **not** complete the assignment for you. You still need to write the main/core code that determines what Karel should actually do.

---

## Functions

### `f_move(num=1)`

Moves Karel forward a specified number of times.

```python
f_move(3)
```

Equivalent to:

```python
move()
move()
move()
```

**Default:**

```python
f_move()
```

Moves Karel once.

---

### `f_left(num=1)`

Turns Karel left a specified number of times.

```python
f_left(2)
```

Equivalent to:

```python
turn_left()
turn_left()
```

**Default:**

```python
f_left()
```

Turns Karel left once.

---

### `f_right(num)`

Turns Karel right a specified number of times.

```python
f_right(1)
```

A right turn is accomplished by turning left three times.

This is useful because basic Karel environments generally provide `turn_left()` but not a built-in `turn_right()`.

> **Note:** `f_right()` currently requires a number to be provided.

---

### `f_place(num=1)`

Places a specified number of balls.

```python
f_place(3)
```

Equivalent to:

```python
put_ball()
put_ball()
put_ball()
```

**Default:**

```python
f_place()
```

Places one ball.

---

### `f_take(num=1)`

Takes a specified number of balls.

```python
f_take(3)
```

Equivalent to:

```python
take_ball()
take_ball()
take_ball()
```

**Default:**

```python
f_take()
```

Takes one ball.

---

### `f_rotate(num=1)`

Rotates Karel **180°** a specified number of times.

```python
f_rotate()
```

Equivalent to:

```python
turn_left()
turn_left()
```

You can also rotate multiple times:

```python
f_rotate(2)
```

---

### `f_backflip(num=1)`

Turns Karel **360°** a specified number of times.

```python
f_backflip()
```

Equivalent to:

```python
turn_left()
turn_left()
turn_left()
turn_left()
```

This leaves Karel facing the same direction as before the turn.

---

## Example

Without the helper functions:

```python
move()
move()
move()
turn_left()
turn_left()
put_ball()
put_ball()
```

With the helper functions:

```python
f_move(3)
f_left(2)
f_place(2)
```

This makes repetitive parts of your code shorter and easier to read.

---

## Important

These functions **do not solve Karel assignments automatically**.

You are still responsible for writing the actual solution logic, including:

* Deciding where Karel needs to go
* Using `if` statements when necessary
* Using `while` loops when necessary
* Checking walls, balls, and other conditions
* Determining when Karel should stop
* Creating the overall algorithm for the assignment

Think of these functions as **extra tools** that make repetitive commands faster to write.

### Recommended Use

Use these functions whenever you find yourself repeatedly writing the same Karel command:

```python
move()
move()
move()
move()
```

can become:

```python
f_move(4)
```

The goal is to reduce repetitive code while keeping the actual assignment-solving logic yours.
