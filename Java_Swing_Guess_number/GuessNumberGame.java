import java.awt.event.*;
import javax.swing.*;

class CreateUI implements ActionListener {
    JTextField numberField;
    JLabel title, result;
    JButton checkButton;
    int finalNum = 1;
    CreateUI() {
        finalNum = getRandomNumber(1, 100);

        JFrame f = new JFrame("Guess Number");

        title = new JLabel();
        title.setBounds(50, 50, 300, 30);
        title.setText("Guess a number between 1 to 100");

        numberField = new JTextField();
        numberField.setBounds(50, 100, 150, 20);

        result = new JLabel();
        result.setBounds(50, 200, 300, 20);
        result.setText("");

        checkButton = new JButton("Check Number");
        checkButton.setBounds(50, 150, 150, 30);
        checkButton.addActionListener(this);

        f.add(title);
        f.add(numberField);
        f.add(result);
        f.add(checkButton);
        f.setSize(375, 300);
        f.setLayout(null);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public int getRandomNumber(int min, int max) {
        return (int) ((Math.random() * (max - min)) + min);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String numString = numberField.getText();

        int num = Integer.parseInt(numString);

        if (e.getSource() == checkButton) {
            if (finalNum == num) {
                result.setText("Congratulations, you guessed the number.");
                finalNum = getRandomNumber(1, 100);
            } else if (finalNum > num) {
                result.setText("The number is larger than " + num);
            } else {
                result.setText("The number is smaller than " + num);
            }
        }
    }
}

public class GuessNumberGame {
    public static void main(String[] args) {
        new CreateUI();
    }
}
