# ECE444-F2023-Lab5
Christopher Mountain's Lab 5 for ECE444

Copy of: https://github.com/mjhea0/flaskr-tdd#test-driven-development


What are the pros and cons of test driven development?

The pros of test driven development are as follows:
1. Automatic Documentation - Test driven development by definition generates a test suite that can give onboarding developers a quick-and-easy
page to look broadly at functions across the application and understand their inputs and expected outputs.
2. Sanity-Checking - TDD makes it more difficult to make stupid, simple mistakes. Well written tests should make it difficult even to make subtle
mistakes. This should, as a rule, reduce the overall errors committed to the codebase.
3. Improving Code Quality - Writing tests also forces developers to think through architecture and edge cases before implementation, 
which is a good mindset while coding and will likely improve code quality.
4. Debugging - When tests fail, it should indicate which services, controllers, and recent code changes are at fault. Ideally this simplifies
debugging across the project.

The cons of TDD are as follows:
1. Slower Development at the Start - when embarking on new features or projects, you slow down your initial rate of development by adding
testing to the task list. However, this may pay off in time saved with more maintainable code later on.
2. Learning TDD. Developers (like me) unfamiliar with TDD will need to learn TDD. This will take time and resources.
3. Having a false sense of security - Having a test suite may make you feel like you have permission to not worry about possible errors your
new code could have, should all tests pass. However, there will be cases that were difficult or subtle that you are not testing for, which
could cause errors you would have otherwise considered without a testing suite.
4. Maintaining Test Cases - As your project grows, you will need to invest time in maintaining test cases, which can be cumbersome.
