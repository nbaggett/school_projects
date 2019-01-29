import processing.core.PImage;
import java.util.List;
import java.util.Optional;

public class MinerNotFull extends Miner
{
    private static final String MINER_KEY = "miner";
    private static final int MINER_NUM_PROPERTIES = 7;
    private static final int MINER_ID = 1;
    private static final int MINER_COL = 2;
    private static final int MINER_ROW = 3;
    private static final int MINER_LIMIT = 4;
    private static final int MINER_ACTION_PERIOD = 5;
    private static final int MINER_ANIMATION_PERIOD = 6;

    private int resourceLimit;
    private int resourceCount;

    public MinerNotFull(String id, Point position, List<PImage> images, int resourceLimit,
                     int resourceCount, int actionPeriod, int animationPeriod)
    {
        super(id, position, images, actionPeriod, animationPeriod);
        this.resourceLimit = resourceLimit;
        this.resourceCount = resourceCount;
    }

    public void incrementResource()
    {
        resourceCount += 1;
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler)
    {
        Optional<Entity> notFullTarget = Movable.findNearest(world, super.getPosition(),
                Ore.class);

        if (!notFullTarget.isPresent() ||
                !moveTo(scheduler, world, notFullTarget.get()) ||
                !transform(world, scheduler, imageStore))
        {
            scheduler.scheduleEvent(this,
                    new Activity(this, world, imageStore),
                    super.getActionPeriod());
        }
    }

    private boolean transform(WorldModel world, EventScheduler scheduler, ImageStore imageStore)
    {
        if (this.resourceCount >= this.resourceLimit)
        {
            MinerFull miner = new MinerFull(super.getId(), super.getPosition(), super.getImages(), 2,
                    this.resourceCount, super.getActionPeriod(), super.getAnimationPeriod());

            this.remove(world);
            scheduler.unscheduleAllEvents(this);

            world.addEntity(miner);
            miner.scheduleActions(scheduler, world, imageStore);

            return true;
        }

        return false;
    }

    @Override
    public void move(WorldModel world, Point pos)
    {
        Point oldPos = this.getPosition();
        if (world.withinBounds(pos) && !pos.equals(oldPos))
        {
            world.setOccupancyCell(oldPos, null);
            removeAt(world, pos);
            world.setOccupancyCell(pos, this);
            super.setPosition(pos);
        }
    }

    public static boolean parse(ImageStore imageStore, String [] properties, WorldModel world)
    {
        if (properties.length == MINER_NUM_PROPERTIES)
        {
            Point pt = new Point(Integer.parseInt(properties[MINER_COL]),
                    Integer.parseInt(properties[MINER_ROW]));
            Entity minerNotFull = new MinerNotFull(properties[MINER_ID],
                    pt,
                    imageStore.getImageList(MINER_KEY),
                    Integer.parseInt(properties[MINER_LIMIT]),
                    0,
                    Integer.parseInt(properties[MINER_ACTION_PERIOD]),
                    Integer.parseInt(properties[MINER_ANIMATION_PERIOD]));
            world.tryAddEntity(minerNotFull);
        }

        return properties.length == MINER_NUM_PROPERTIES;
    }
}
