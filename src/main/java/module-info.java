module com.example.facultyadjunctmanagementapp {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;

    opens com.example.facultyadjunctmanagementapp to javafx.fxml;
    exports com.example.facultyadjunctmanagementapp;
}