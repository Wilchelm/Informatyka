<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">

<html>
<body>


	<xsl:for-each select="czlowiek/osoba">
	<div width="40%">
	
		<xsl:value-of select="imie"/><br />
		
		<xsl:value-of select="nazwisko"/><br />
		
		<xsl:value-of select="urodziny"/><br />
		
		<xsl:value-of select="email"/><br />
		
		<xsl:value-of select="wzrost"/><br />
		
		<xsl:value-of select="numer1"/><br />
		
		<xsl:value-of select="numer2"/><br />
		
		<xsl:value-of select="numer3"/><br />
		
		<xsl:value-of select="plec"/><br />
	</div>
<hr/>	
	
	
	

</xsl:for-each>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
		
		