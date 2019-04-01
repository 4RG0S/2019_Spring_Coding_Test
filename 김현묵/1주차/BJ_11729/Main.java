import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

	static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void move(int num, int start, int end, int nam) throws IOException {

		if (num == 0) {

		} else {
			move(num - 1, start, nam, end);
			writer.write(start + " " + end + "\n");
			move(num - 1, nam, end, start);
		}

	}
/*
	public static int numbering(int num) {
		if (num == 3) {
			return 7;
		} else {
			return numbering(num - 1) + numbering(num - 1) + 1;
		}
	}
	*/

	public static void main(String[] args) throws IOException {

		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

		String input = reader.readLine();

		int pan = Integer.parseInt(input);
		int numbering = (int) Math.pow(2, pan) -1;
		writer.write(Integer.toString(numbering) + "\n");

		move(pan, 1, 3, 2);
		// writer.write(buffer.toString());

		writer.flush();
		writer.close();

	}
}
