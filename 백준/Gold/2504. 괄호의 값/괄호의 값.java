import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException { 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        System.out.println(calculateBracketValue(s));
    }

    public static int calculateBracketValue(String s) {
        Stack<Character> stack = new Stack<>();
        int value = 0;
        int tempMultiplier = 1; // 현재 괄호 묶음의 곱셈 값

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == '(') {
                stack.push(ch);
                tempMultiplier *= 2;
            } else if (ch == '[') {
                stack.push(ch);
                tempMultiplier *= 3;
            } else if (ch == ')') {
                // 스택이 비어있거나 짝이 맞지 않으면 올바르지 않은 괄호열
                if (stack.isEmpty() || stack.peek() != '(') {
                    return 0;
                }
                // 바로 직전 괄호가 '()' 형태이면 값 추가
                if (s.charAt(i - 1) == '(') {
                    value += tempMultiplier;
                }
                stack.pop();
                tempMultiplier /= 2; // 괄호를 닫았으므로 곱셈 값 되돌리기
            } else if (ch == ']') {
                if (stack.isEmpty() || stack.peek() != '[') {
                    return 0;
                }
                // 바로 직전 괄호가 '[]' 형태이면 값 추가
                if (s.charAt(i - 1) == '[') {
                    value += tempMultiplier;
                }
                stack.pop();
                tempMultiplier /= 3; // 괄호를 닫았으므로 곱셈 값 되돌리기
            }
        }

        // 모든 괄호를 다 처리한 후 스택이 비어있지 않으면 올바르지 않은 괄호열
        if (!stack.isEmpty()) {
            return 0;
        }

        return value;
    }
}