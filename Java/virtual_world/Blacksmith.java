import processing.core.PImage;

import java.util.List;

public class Blacksmith extends Entity
{
    private static final String SMITH_KEY = "blacksmith";
    private static final int SMITH_NUM_PROPERTIES = 4;
    private static final int SMITH_ID = 1;
    private static final int SMITH_COL = 2;
    private static final int SMITH_ROW = 3;

    public Blacksmith(String id, Point position, List<PImage> images)
    {
        super(id, position, images);
    }

    public static boolean parse(ImageStore imageStore, String [] properties, WorldModel world)
    {
        if (properties.length == SMITH_NUM_PROPERTIES)
        {
            Point pt = new Point(Integer.parseInt(properties[SMITH_COL]),
                    Integer.parseInt(properties[SMITH_ROW]));
            Entity entity = new Blacksmith(properties[SMITH_ID], pt, imageStore.getImageList(SMITH_KEY));//)createBlacksmith(properties[SMITH_ID], pt, this.getImageList(SMITH_KEY));
            world.tryAddEntity(entity);
        }

        return properties.length == SMITH_NUM_PROPERTIES;
    }
}