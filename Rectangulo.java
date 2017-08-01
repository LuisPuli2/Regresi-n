/* Clase para crear rectángulos. */

public class Rectangulo{

	//Atributos
	Punto p1;
	Punto p2;

	// Constructor
	public Rectangulo(double x1, double y1, double x2, double y2){
		p1 = new Punto(x1,y1);
		p2 = new Punto(x2,y2);
	}

	public void desplaza_horizontal (double distancia){
		this.p1.aumentaX(distancia);
		this.p2.aumentaX(distancia);
	}

	public void desplaza_vertical (double distancia){
		this.p1.aumentaY(distancia);
		this.p2.aumentaY(distancia);
	}

	// Funciones auxiliares
	public double minimo (double a,double b){
		if(a<b)
			return a;
		return b;
	}

	public double maximo (double a,double b){
		if (a>b)
			return a;
		return b; 
	}

	public double encuentra_min_x(Rectangulo r){
		double aux1 = minimo(r.p1.x,r.p2.x);
		double aux2 = minimo(this.p1.x,this.p2.x);
		return minimo(aux1,aux2);
	}

	public double encuentra_max_x(Rectangulo r){
		double aux1 = maximo(r.p1.x,r.p2.x);
		double aux2 = maximo(this.p1.x,this.p2.x);
		return maximo(aux1,aux2);
	}

	public double encuentra_min_y(Rectangulo r){
		double aux1 = minimo(r.p1.x,r.p2.x);
		double aux2 = minimo(this.p1.x,this.p2.x);
		return minimo(aux1,aux2);
	}

	public double encuentra_max_y(Rectangulo r){
		double aux1 = maximo(r.p1.y,r.p2.y);
		double aux2 = maximo(this.p1.y,this.p2.y);
		return maximo(aux1,aux2);
	}

	public void union (Rectangulo r){
		double x1 = this.encuentra_min_x(r);
		double y1 = this.encuentra_min_y(r);
		double x2 = this.encuentra_max_x(r);
		double y2 = this.encuentra_max_y(r);
		System.out.println("Las coordendas son: ");
		System.out.println(x1+","+y1+ " y " + x2 + "," +y2);
		/*return new Rectangulo(x1,y1,x2,y2);*/
	}

	public void interseccion (Rectangulo r){
		Punto x1 = this.p1.mayor(r.p1);
		Punto x2 = this.p2.menor(r.p2);
		if (x1.esMayor(x2)){
			System.out.println(" No hay intersección");
		} else{
			System.out.println("Si hay intersección");
			System.out.println("Las coordendas son: ");
			System.out.println(x1.x+","+x1.y+ " y " + x2.x + "," +x2.y);
		}
	}

	public static void main(String[] args) {
		/* Pruebas */
		Rectangulo r1 = new Rectangulo(2,2,4,4);
		Rectangulo r2 = new Rectangulo(3,3,5,5);
		r1.union(r2);
		r1.interseccion(r2);

		/* Más pruebas */

		Rectangulo r3 = new Rectangulo(2,2,4,4);
		Rectangulo r4 = new Rectangulo(5,5,8,7);
		r3.union(r4);
		r3.interseccion(r4);
	}

}
