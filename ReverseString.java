/**
 * Write a function to reverse a String in place.
 * Since Java Strings are immutable. We will have to use a
 * character array for this problem.
 */
public class ReverseString {

  static void reverseStringInPlace (char[] word) {
    int i = 0; // Start position
    int j = word.length - 1; // Last position

    while (i < j) {
      char temp = word[i];
      word[i] = word[j];
      word[j] = temp;
      i++;
      j--;
    }
  }

  /**
   * Tests from video
   */
  public static void main (String[] args) {
    String t1 = "James";
    String t2 = "botTle";
    String t3 = "a";

    char [] a1 = t1.toCharArray();
    char [] a2 = t2.toCharArray();
    char [] a3 = t3.toCharArray();

    reverseStringInPlace(a1);
    reverseStringInPlace(a2);
    reverseStringInPlace(a3);

    System.out.println(a1);
    System.out.println(a2);
    System.out.println(a3);
  }

}
