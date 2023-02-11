package dtas;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HashingTool
{

    public static String sha512(String subject)
    {
        try
        {
            MessageDigest md = MessageDigest.getInstance("SHA-512");
            md.update(subject.getBytes());

            byte byteData[] = md.digest();

            StringBuilder sb = new StringBuilder();
            for (byte aByteData : byteData)
            {
                sb.append(Integer.toString((aByteData & 0xff) + 0x100, 16).substring(1));
            }

            return sb.toString();
        }
        catch (NoSuchAlgorithmException ignored)
        {
            return "";
        }
    }
}
