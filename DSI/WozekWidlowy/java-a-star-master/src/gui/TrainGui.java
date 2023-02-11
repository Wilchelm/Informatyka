package gui;


import data.GoodOutputs;

import data.GoodPixels;
import data.ReadWriteFile;
import game.Game;
import gui.components.CustomPanel;
import gui.components.DrawingPanel;
import neuron.Train;
import neuron.TrainingSet;

import javax.swing.*;
import java.awt.*;
import java.io.Console;
import java.util.ArrayList;



public class TrainGui extends JFrame {

    private final int RESOLUTION = 20;

    private Train networkTrainer;

    private JPanel mainPanel;
    private DrawingPanel drawingPanel;
    private CustomPanel resultPanel;

    private JButton clearButton;
    private JButton trainButton;
    private JButton transformButton;
    private JButton helpButton;
    private JButton trainNetworkButton;
    private JButton drawLetterButton;
    private JButton somethingButton;
    private JButton changeButton;
    private JTextField somethingText;
    private JTextField trainingSetsAmount;
    private JComboBox<String> drawLetterCombo;
    private JComboBox<String> trainAsCombo;
    private JTextArea outputTextArea;
    private char parametr;
    
    private Game game;


    public TrainGui() {
        super("Rozpoznawanie symbolu");

        networkTrainer = new Train();

        setMainPanel();
        setLeftSide();
        setCenterArea();
        setRightSide();
        setOutputPanel();

        setOnClicks();

        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setVisible(true);
        setSize(new Dimension(1260, 500));
        setLocationRelativeTo(null);
        setResizable(false);
    }
    
    public TrainGui(Game game) {
        super("Rozpoznawanie symbolu");

        networkTrainer = new Train();
        this.game=game;

        setMainPanel();
        setLeftSide();
        setCenterArea();
        setRightSide();
        setOutputPanel();

        setOnClicks();

        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setVisible(true);
        setSize(new Dimension(1260, 500));
        setLocationRelativeTo(null);
        setResizable(false);
    }

    public char getParametr() {
		return parametr;
	}

	public void setParametr(char parametr) {
		this.parametr = parametr;
	}

	private void setMainPanel() {
        mainPanel = new JPanel();
        mainPanel.setBackground(Color.LIGHT_GRAY);
        setContentPane(mainPanel);
    }

    private void setLeftSide() {
        JPanel panel = new JPanel();
        panel.setBackground(Color.LIGHT_GRAY);
        panel.setPreferredSize(new Dimension(410, 440));

        drawLetterButton = new JButton("Rysuj:");
        drawLetterCombo = new JComboBox<>(new String[]{"A - G�ra","B- Chroni� przed wilgoci�","C - Uwaga szk�o"});

        drawingPanel = new DrawingPanel(400, 400, RESOLUTION);

        panel.add(drawLetterButton);
        panel.add(drawLetterCombo);
        panel.add(drawingPanel);

        mainPanel.add(panel);
    }

    private void setCenterArea() {
    	
        JPanel centerPanel = new JPanel();
        centerPanel.setLayout(new GridBagLayout());
        centerPanel.setPreferredSize(new Dimension(250, 450));
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridwidth = GridBagConstraints.REMAINDER;
        gbc.anchor = GridBagConstraints.CENTER;
        
        centerPanel.add(new JLabel("Trenuj sie� jako:", SwingConstants.CENTER), gbc); 
        trainAsCombo = new JComboBox<>(new String[]{"A - G�ra","B- Chroni� przed wilgoci�","C - Uwaga szk�o"});
        trainAsCombo.setAlignmentX(Component.CENTER_ALIGNMENT);
        trainAsCombo.setMaximumSize(new Dimension((int) trainAsCombo.getPreferredSize().getWidth(), 30));
        
        trainingSetsAmount = new JFormattedTextField();
        trainingSetsAmount.setText("5000");
        trainingSetsAmount.setMaximumSize(new Dimension(250, 50));
        trainingSetsAmount.setAlignmentX(Component.CENTER_ALIGNMENT);
        
        trainButton = new JButton("                        Train                        ");
        
        trainNetworkButton = new JButton("                Trenuj X razy:                ");
        
        transformButton = new JButton("                   Rozpoznaj                   ");
        
        clearButton =     new JButton("             <= Wyczy�� pole             ");
        
        changeButton = new JButton("ZMIE� SYMBOL PACZKI NA =>");
        changeButton.setForeground(Color.red);
        
        centerPanel.add(Box.createVerticalStrut(50));
        centerPanel.add(trainAsCombo, gbc);
        centerPanel.add(Box.createVerticalStrut(50));
        centerPanel.add(trainButton, gbc);
        centerPanel.add(trainingSetsAmount, gbc);
        centerPanel.add(trainNetworkButton, gbc);
        centerPanel.add(Box.createVerticalStrut(50));
        centerPanel.add(transformButton, gbc);       
        centerPanel.add(clearButton, gbc);
        centerPanel.add(Box.createVerticalStrut(100));
        centerPanel.add(changeButton , gbc);

        mainPanel.add(centerPanel);
    }

    private void setRightSide() {
        JPanel panel = new JPanel();
        panel.setBackground(Color.LIGHT_GRAY);
        panel.setBorder(BorderFactory.createEmptyBorder(30, 0, 0, 0));
        resultPanel = new CustomPanel(400, 400, RESOLUTION);
        
        panel.add(resultPanel);  
        mainPanel.add(panel);
    }

    private void setOutputPanel() {
        JPanel outputPanel = new JPanel();
        outputPanel.setPreferredSize(new Dimension(150, 430));

        outputTextArea = new JTextArea();
        outputTextArea.setPreferredSize(new Dimension(150, 430));
        outputPanel.add(outputTextArea);

        mainPanel.add(outputPanel);
    }

    private void setOnClicks() {
        clearButton.addActionListener(e -> drawingPanel.clear());

        trainButton.addActionListener(e -> {
            String letter = (String) trainAsCombo.getSelectedItem();
            networkTrainer.addTrainingSet(new TrainingSet(drawingPanel.getPixels(), GoodOutputs.getInstance().getGoodOutput(letter)));
            ReadWriteFile.saveToFile(drawingPanel.getPixels(), letter);
        });

        transformButton.addActionListener(e -> {
            networkTrainer.setInputs(drawingPanel.getPixels());

            ArrayList<Double> outputs = networkTrainer.getOutputs();
            int index = 0;
            for (int i = 0; i < outputs.size(); i++) {
                if (outputs.get(i) > outputs.get(index))
                    index = i;
            }

            updateTextArea();

            trainAsCombo.setSelectedIndex(index);
            resultPanel.drawLetter(GoodPixels.getInstance().getGoodPixels(index));
        });

        trainNetworkButton.addActionListener(e -> {
            int number = 0;
            try {
                number = Integer.parseInt(trainingSetsAmount.getText());
            } catch (Exception x) {
                JOptionPane.showMessageDialog(this, "Z�a liczba albo wyst�puj� puste znaki", "ERROR", JOptionPane.PLAIN_MESSAGE);
            }

            networkTrainer.train(number);
        });

        drawLetterButton.addActionListener(e -> {
            String letter = (String) drawLetterCombo.getSelectedItem();
            ArrayList<Integer> goodPixels = GoodPixels.getInstance().getGoodPixels(letter);
            drawingPanel.drawLetter(goodPixels);
        });

        drawLetterCombo.addActionListener(e -> {
            String letter = (String) drawLetterCombo.getSelectedItem();
            ArrayList<Integer> goodPixels = GoodPixels.getInstance().getGoodPixels(letter);
            drawingPanel.drawLetter(goodPixels);
        });
        
        changeButton.addActionListener(e -> {
        	String letter = (String) trainAsCombo.getSelectedItem();
        	game.getTour().getPack(0).setSymbol(letter.charAt(0));
        	
        	
        });

    }

    private void updateTextArea() {
        StringBuilder sb = new StringBuilder();
        ArrayList<Double> outputs = networkTrainer.getOutputs();
        for (int i = 0; i < outputs.size(); i++) {
            int letterValue = i + 65;
            sb.append((char) letterValue);
            double value = outputs.get(i);
            if (value < 0.01)
                value = 0;
            if (value > 0.99)
                value = 1;

            value *= 1000;
            int x = (int) (value);
            value = x / 1000.0;

            sb.append("\t " + value);
            sb.append("\n");
        }
        outputTextArea.setText(sb.toString());
    }

}

