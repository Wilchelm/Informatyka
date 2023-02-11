
import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.FunctionBlock;

import net.sourceforge.jFuzzyLogic.Gpr;

import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;

import net.sourceforge.jFuzzyLogic.rule.Variable; 


public class klasyfikator {

	public static void main(String[] args) throws Exception {
		// Load from 'FCL' file
		String fileName = "./klasyfikator.fcl";
		FIS fis = FIS.load(fileName, true);
		if( fis == null ) { 
			System.err.println("Nie moge zaladowc pliku: '" + fileName + "'");
			return;
		}

		// Pokazuje reguly
		FunctionBlock functionBlock = fis.getFunctionBlock(null);
	        JFuzzyChart.get().chart(functionBlock);	

		// Ustawia wejscia
		fis.setVariable("wiek", 3);
		fis.setVariable("doswiadczenie", 3);
		fis.setVariable("inteligencja", 8);

		// Wylicza zbiory rozmyte
		fis.evaluate();

		// Ustawia wyjscia
		Variable klasyfikator = functionBlock.getVariable("klasyfikator");		

		// Pokazuje wykres zmiennych wyjsciowych

		JFuzzyChart.get().chart(klasyfikator, klasyfikator.getDefuzzifier(), true);
		
		// Drukuje reguly
		System.out.println(fis);
		System.out.println("klasyfikator:" + fis.getVariable("klasyfikator").getValue()); 
	}
}
