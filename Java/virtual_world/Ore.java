import processing.core.PImage;

import java.util.List;
import java.util.Random;

public class Ore extends ActiveEntity
{
    private static final String ORE_KEY = "ore";
    private static final int ORE_NUM_PROPERTIES = 5;
    private static final int ORE_ID = 1;
    private static final int ORE_COL = 2;
    private static final int ORE_ROW = 3;
    private static final int ORE_ACTION_PERIOD = 4;

    private static final String BLOB_KEY = "blob";
    private static final String BLOB_ID_SUFFIX = " -- blob";
    private static final int BLOB_PERIOD_SCALE = 4;
    private static final int BLOB_ANIMATION_MIN = 50;
    private static final int BLOB_ANIMATION_MAX = 150;
    private static final Random rand = new Random();

    public Ore(String id, Point position, List<PImage> images, int actionPeriod)
    {
        super(id, position, images, actionPeriod);
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler)
    {
        Point pos = super.getPosition();  // store current position before removing

        this.remove(world);
        scheduler.unscheduleAllEvents(this);

        OreBlob blob = new OreBlob(super.getId() + BLOB_ID_SUFFIX, pos, imageStore.getImageList(BLOB_KEY),super.getActionPeriod() / BLOB_PERIOD_SCALE,
                BLOB_ANIMATION_MIN + rand.nextInt(BLOB_ANIMATION_MAX - BLOB_ANIMATION_MIN));

        world.addEntity(blob);
        blob.scheduleActions(scheduler, world, imageStore);
    }

    public static boolean parse(ImageStore imageStore, String [] properties, WorldModel world)
    {
        if (properties.length == ORE_NUM_PROPERTIES)
        {
            Point pt = new Point(Integer.parseInt(properties[ORE_COL]),
                    Integer.parseInt(properties[ORE_ROW]));
            Entity ore = new Ore(properties[ORE_ID],
                    pt,
                    imageStore.getImageList(ORE_KEY),
                    Integer.parseInt(properties[ORE_ACTION_PERIOD]));
            world.tryAddEntity(ore);
        }

        return properties.length == ORE_NUM_PROPERTIES;
    }
}
