%{
#include <stdio.h>
%}

%%
 
"run"|"walk"|"eat"|"sleep"|"divide" { printf("Verb : %s\n", yytext); }
 
"I"|"you"|"he"|"she"|"it"|"we"|"they" { printf("Pronoun : %s\n", yytext); }
 
"quickly"|"slowly"|"happily"|"sadly"|"strong"|"dramatic"|"toward"|"binary"|"into"|"distinct" { printf("Adverb : %s\n", yytext); }
 
"dog"|"cat"|"car"|"tree"|"instinct"|"urge"|"things"|"groups"|"gap" { printf("Noun : %s\n", yytext); }
 
[[:alpha:]]+ly { printf("Adverb : %s\n", yytext); } // Catch adverbs ending in "ly"
 
[[:alpha:]]+ { printf("Unknown : %s\n", yytext); } // Catch other words
 
[\n\t ]+ { /* Ignore whitespace, newline, tab */ }
 
. { printf("Unknown : %s\n", yytext); }
 
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
