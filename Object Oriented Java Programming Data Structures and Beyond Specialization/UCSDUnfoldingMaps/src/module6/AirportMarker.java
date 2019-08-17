package module6;

import java.util.List;

import de.fhpotsdam.unfolding.data.Feature;
import de.fhpotsdam.unfolding.data.PointFeature;
import de.fhpotsdam.unfolding.marker.SimpleLinesMarker;
import processing.core.PConstants;
import processing.core.PGraphics;

/** 
 * A class to represent AirportMarkers on a world map.
 *   
 * @author Adam Setters and the UC San Diego Intermediate Software Development
 * MOOC team
 *
 */
public class AirportMarker extends CommonMarker {
	public static List<SimpleLinesMarker> routes;
	
	public AirportMarker(Feature city) {
		super(((PointFeature)city).getLocation(), city.getProperties());
	
	}
	
	@Override
	public void drawMarker(PGraphics pg, float x, float y) {
		
		pg.fill(11);
		pg.ellipse(x, y, 5, 5);
		
		//buffer.beginDraw();
//		buffer.fill(11);
//		buffer.ellipse(x, y, 5, 5);
		//buffer.endDraw();

		
		
	}

	@Override
	public void showTitle(PGraphics pg, float x, float y) {
		
		String airportName = this.getName();
		String airportCity = this.getCity();
		String airportCountry = this.getCountry();
		String airportAlt = this.getAltitude();
		
		String aiportInfo = airportName + " in " + airportCity + ", " + airportCountry
				+ " at " + airportAlt + "ft";
		
		pg.pushStyle();
		
		pg.rectMode(PConstants.CORNER);
		pg.stroke(110);
		pg.fill(255,255,255);
		pg.rect(x, y + 15, pg.textWidth(aiportInfo) +6, 18, 5);
		
		pg.textAlign(PConstants.LEFT, PConstants.TOP);
		pg.fill(0);
		pg.text(aiportInfo, x + 3 , y +18);
		
		
		pg.popStyle();
		 // show rectangle with title
		
		// show routes
		
		
	}
	
	
	public String getName() {
		return (String) this.getProperty("name");	
		
	}
	
	public String getCity() {
		return (String) this.getProperty("city");	
		
	}
	
	public String getCountry() {
		return (String) this.getProperty("country");	
		
	}
	
	public String getAltitude() {
		return (String) this.getProperty("altitude");	
		
	}
}
