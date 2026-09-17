import java.io.*;
import java.net.*;

public class ClientUDP
{
	public static void main( String[] args )
	{
		try
		{
			InetAddress addr = InetAddress.getLocalHost();
			System.out.println( "adresse=" + addr.getHostName() );

			String s = "Hello World";
			byte[] data = s.getBytes();

			DatagramPacket packet = new DatagramPacket( data, data.length, addr, 1234 );
			DatagramSocket sock = new DatagramSocket();
			sock.send( packet );

			DatagramPacket reponse = new DatagramPacket( new byte[1024], 1024 );
			sock.receive( reponse );
			String str = new String( reponse.getData() );
			System.out.println( "reponse=" + str );

			sock.close();
		}
		catch( Exception ex )
		{
			System.out.println( "erreur !" );
			ex.printStackTrace();
		}
	}
}