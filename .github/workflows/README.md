Dependency Review Action:
This Action will scan dependency manifest files that change as part of a Pull Reqest, surfacing known-vulnerable versions of the packages declared or updated in the PR. 
Once installed, if the workflow run is marked as required, PRs introducing known-vulnerable packages will be blocked from merging.

CodeQL Analysis:
CodeQL is the analysis engine used by developers to automate security checks, and by security researchers to perform variant analysis.
In CodeQL, code is treated like data. Security vulnerabilities, bugs, and other errors are modeled as queries that can be executed against databases extracted from code. You can run the standard CodeQL queries, written by GitHub researchers and community contributors, or write your own to use in custom analyses. Queries that find potential bugs highlight the result directly in the source file. (Code QL supports analysis for C/C++, C#, Go, Java, Kotlin, JavaScript, Python, Ruby and Typescript)
