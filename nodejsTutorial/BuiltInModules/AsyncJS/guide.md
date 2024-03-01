# Asynchronous JS

- JS is a synchronous, blocking, single-threaded language.
- This nature however is not beneficial for writing apps.
- We want non-blocking asynchronous behavior which is made possible by the browser for Frontend and Node.js for backends.
- This style of programming where we don't block the main JS thread is fundamental to Node.js and is at the heart of the of how some of the built-in module code is written.

## Synchronous

- If we have two functions which log messages to the console, code executes top down, with only one line executing at any given time.

## Blocking

- No matter how long the previous process takes, the subsequent processes won't kick off until the former is done.

## Single-threaded

- A thread is simply a process that your javascript program can use to run a task.
- Each thread can only do one task at a time.
- JavaScript has a single-threaded called main thread for execution of any code.
