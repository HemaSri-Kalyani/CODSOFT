import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

public class NotificationDemo extends Application {

    private static final String NOTIFICATION_TITLE = "Demo Notification";
    private static final String NOTIFICATION_MESSAGE = "This is a sample notification.";

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Java Notification Demo");

        HBox notificationBox = createNotification();

        Scene scene = new Scene(notificationBox);
        primaryStage.setScene(scene);

        // Set the stage style to transparent
        primaryStage.initStyle(StageStyle.TRANSPARENT);

        // Move the notification to the bottom-right corner of the screen
        primaryStage.setX(Screen.getPrimary().getVisualBounds().getMaxX() - 300);
        primaryStage.setY(Screen.getPrimary().getVisualBounds().getMaxY() - 100);

        primaryStage.show();
    }

    private HBox createNotification() {
        HBox notificationBox = new HBox(10);
        notificationBox.setAlignment(Pos.CENTER);
        notificationBox.setStyle("-fx-background-color: #3498db; -fx-padding: 10; -fx-border-radius: 10;");

        // Add an optional image/icon to the notification
        ImageView imageView = new ImageView(new Image("icon.png")); // Replace "icon.png" with your image file
        imageView.setFitWidth(30);
        imageView.setFitHeight(30);

        Label titleLabel = new Label(NOTIFICATION_TITLE);
        titleLabel.setStyle("-fx-text-fill: white; -fx-font-weight: bold;");

        Label messageLabel = new Label(NOTIFICATION_MESSAGE);
        messageLabel.setStyle("-fx-text-fill: white;");

        notificationBox.getChildren().addAll(imageView, titleLabel, messageLabel);

        // Allow the user to close the notification by clicking on it
        notificationBox.setOnMouseClicked(event -> StageHelper.getStages().forEach(Stage::close));

        return notificationBox;
    }
}
