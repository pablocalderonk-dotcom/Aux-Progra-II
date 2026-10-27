package comp.agrega;

import java.util.ArrayList;
import java.util.Scanner;

public class COmpAgrega {
    public static void main(String[] args) {
        Scanner te = new Scanner(System.in);
        
        // a. Instanciar N objetos Laptop en un vector
        ArrayList<Laptop> vec = new ArrayList<>();
        Laptop lap = new Laptop("samsung", 0, "lcd ips", 13, 7);
        lap.agregaApp(new Aplicacion("Word", 200));
        lap.agregaApp(new Aplicacion("Excel", 150));
        
        Laptop lap1 = new Laptop("hp", 0, "oled", 15, 9);
        lap1.agregaApp(new Aplicacion("Photoshop", 500));
        
        Laptop lap2 = new Laptop("lenovo", 0, "amoled", 13, 7);
        lap2.agregaApp(new Aplicacion("Chrome", 300));
        lap2.agregaApp(new Aplicacion("VSCode", 250));
        lap2.agregaApp(new Aplicacion("Zoom", 100));
        
        vec.add(lap);
        vec.add(lap1);
        vec.add(lap2);

        // b. Mostrar la laptop que tenga mas aplicaciones
        System.out.println("--- b. Laptop con mas apps ---");
        Laptop mayor = vec.get(0);
        for (Laptop l : vec) {
            if (l.getCantApp() > mayor.getCantApp()) {
                mayor = l;
            }
        }
        System.out.println(mayor);

        // c. Agregar una aplicacion a la laptop de modelo X
        System.out.println("\n--- c. Agregar app ---");
        System.out.print("Ingrese modelo X: ");
        String x = te.nextLine();
        for (Laptop l : vec) {
            if (l.getModelo().equalsIgnoreCase(x)) { // NO uses ==
                System.out.print("Nombre nueva app: ");
                String nom = te.nextLine();
                System.out.print("Tamanio nueva app: ");
                int tam = Integer.parseInt(te.nextLine());
                l.agregaApp(new Aplicacion(nom, tam));
                System.out.println("Agregada a " + l.getModelo());
            }
        }

        // d. Eliminar todas las aplicaciones de la laptop con pantalla de ancho Y
        System.out.println("\n--- d. Eliminar apps por ancho Y ---");
        System.out.print("Ingrese ancho Y: ");
        int y = Integer.parseInt(te.nextLine());
        for (Laptop l : vec) {
            if (l.getPantalla().getAncho() == y) {
                l.eliminarApps();
                System.out.println("Apps eliminadas de: " + l.getModelo());
            }
        }

        // e. Mostrar a laptop que tiene mas aplicaciones (de nuevo despues de eliminar)
        System.out.println("\n--- e. Laptop con mas apps (actualizado) ---");
        mayor = vec.get(0);
        for (Laptop l : vec) {
            if (l.getCantApp() > mayor.getCantApp()) {
                mayor = l;
            }
        }
        System.out.println(mayor);

        // f. Ordenar de forma decreciente las aplicaciones de cada laptop
        System.out.println("\n--- f. Apps ordenadas ---");
        for (Laptop l : vec) {
            l.ordenarApps();
            System.out.println(l);
        }
    }
}