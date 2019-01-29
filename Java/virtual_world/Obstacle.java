import processing.core.PImage;
import java.util.List;

public class Obstacle extends Entity
{
    private static final String OBSTACLE_KEY = "obstacle";
    private static final int OBSTACLE_NUM_PROPERTIES = 4;
    private static final int OBSTACLE_ID = 1;
    private static final int OBSTACLE_COL = 2;
    private static final int OBSTACLE_ROW = 3;

    public Obstacle(String id, Point position, List<PImage> images)
    {
        super(id, position, images);
    }

    public static boolean parse(ImageStore imageStore, String [] properties, WorldModel world)
    {
        if (properties.length == OBSTACLE_NUM_PROPERTIES)
        {
            Point pt = new Point(
                    Integer.parseInt(properties[OBSTACLE_COL]),
                    Integer.parseInt(properties[OBSTACLE_ROW]));
            Entity entity = new Obstacle(properties[OBSTACLE_ID],pt, imageStore.getImageList(OBSTACLE_KEY));
            world.tryAddEntity(entity);
        }

        return properties.length == OBSTACLE_NUM_PROPERTIES;
    }
}
