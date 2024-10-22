
// /*

// In any language program mostly syntax error occurs due to unbalancing delimiter such as
// (),{},[]. Write C++ program using stack to check whether given expression is well parenthesized or not.
// */


// #include <iostream>
// using namespace std;
// #define size 10

// class stackexp
// {
//     int top;
//     char stk[size];
// public:
//     stackexp()
//     {
//      top=-1;
//     }
//     void push(char);
//     char pop();
//     int isfull();
//     int isempty();
// };

// void stackexp::push(char x)
// {
//     top=top+1;
//     stk[top]=x;
// }

// char stackexp::pop()
// {
//     char s;
//     s=stk[top];
//     top=top-1;
//     return s;
// }

// int stackexp::isfull()
// {
//     if(top==size)
//         return 1;
//     else
//         return 0;
// }

// int stackexp::isempty()
// {
//     if(top==-1)
//         return 1;
//     else
//         return 0;
// }

// int main()
// {
//     stackexp s1;
//     char exp[20],ch;
//     int i=0;
//     cout << "\n\t!! Parenthesis Checker..!!!!" << endl; // prints !!!Hello World!!!
//     cout<<"\nEnter the expression to check whether it is in well form or not :  ";
//     cin>>exp;
//     if((exp[0]==')')||(exp[0]==']')||(exp[0]=='}'))
//     {
//         cout<<"\n Invalid Expression.....\n";
//         return 0;
//     }
//     else
//     {
//         while(exp[i]!='\0')
//         {
//             ch=exp[i];
//             switch(ch)
//             {
//             case '(':s1.push(ch);break;
//             case '[':s1.push(ch);break;
//             case '{':s1.push(ch);break;
//             case ')':s1.pop();break;
//             case ']':s1.pop();break;
//             case '}':s1.pop();break;
//             }
//             i=i+1;
//         }
//     }
//     if(s1.isempty())
//     {
//         cout<<"\nExpression is well parenthesised...\n";
//     }
//     else
//     {
//         cout<<"\nSorry !!! Invalid Expression or not in well parenthesized....\n";
//     }
//     return 0;
// }



#include <iostream>
using namespace std;
#define size 10

class StackExp {
    int top;
    char stk[size];

public:
    StackExp() {
        top = -1;
    }

    void push(char x) {
        if (!isFull()) {
            top = top + 1;
            stk[top] = x;
        } 
        else {
            cout << "Stack Overflow!" << endl;
        }
    }

    char pop() {
        if (!isEmpty()) {
            char s = stk[top];
            top = top - 1;
            return s;
        } else {
            return '\0'; // Return null character if stack is empty
        }
    }

    int isFull() {
        return top == size - 1;
    }

    int isEmpty() {
        return top == -1;
    }
};

bool isMatchingPair(char open, char close) {
    return (open == '(' && close == ')') ||
           (open == '{' && close == '}') ||
           (open == '[' && close == ']');
}

int main() {
    StackExp s1;
    char exp[20], ch;
    int i = 0;

    cout << "\n\t!! Parenthesis Checker..!!!!" << endl;
    cout << "\nEnter the expression to check whether it is well-formed or not: ";
    cin >> exp;

    while (exp[i] != '\0') {
        ch = exp[i];
        switch (ch) {
            case '(': case '[': case '{':
                s1.push(ch);
                break;
            case ')': case ']': case '}':
                if (s1.isEmpty() || !isMatchingPair(s1.pop(), ch)) {
                    cout << "\nInvalid Expression.\n";
                    return 0;
                }
                break;
        }
        i++;
    }

    if (s1.isEmpty()) {
        cout << "\nExpression is well parenthesized.\n";
    } else {
        cout << "\nInvalid Expression: Unmatched opening parentheses.\n";
    }

    return 0;
}
