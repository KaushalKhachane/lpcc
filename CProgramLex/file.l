%{
#include <stdio.h>
%}

%%
"int" { printf("Data Type: %s\n", yytext); }
"float" { printf("Data Type: %s\n", yytext); }
"char" { printf("Data Type: %s\n", yytext); }
"total"|"i" { printf("Variable Name: %s\n", yytext); }
"=" { printf("Assignment Operator: %s\n", yytext); }
"printf" { printf("Function to print: %s\n", yytext); }
"(" { printf("Opening Bracket: %s\n", yytext); }
")" { printf("Closing Bracket: %s\n", yytext); }
"-" { printf("Subtraction Operator: %s\n", yytext); }
";" { printf("Statement Terminator: %s\n", yytext); }
[\n\t ]+ { /* Ignore whitespace, newline, tab */ }
. { }

%%

int yywrap() {
    return 1;
}

int main() {
   yyin = fopen("input.txt", "r");
 
	yylex();
	fclose(yyin);
	yywrap();
	return 0;
}
