import processing.core.PImage;
import java.util.List;
import java.util.Optional;

public class Snowman extends AnimatedEntity
{
    private static final String FROZEN_MINER_KEY = "frozenminer";

    public Snowman(String id, Point position, List<PImage> images,int actionPeriod, int animationPeriod) {
        super(id, position, images, actionPeriod, animationPeriod);
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler)
    {
        Optional<Entity> minerTarget = Movable.findNearest(world, super.getPosition(),
                Miner.class);

        if ((minerTarget.isPresent() && moveTo(scheduler, world, minerTarget.get())))
        {
            transform(world, scheduler, imageStore);
        }

        else {
            Background b = new Background("icegrass", imageStore.getImageList(VirtualWorld.ICEGRASS_KEY));
            world.setBackgroundCell(getPosition(), b);
            scheduler.scheduleEvent(this,
                    new Activity(this, world, imageStore),
                    super.getActionPeriod());
        }
    }

    private void transform(WorldModel world, EventScheduler scheduler, ImageStore imageStore) {
        FrozenMiner frozenMiner = new FrozenMiner(super.getId(), super.getPosition(), imageStore.getImageList(FROZEN_MINER_KEY));

        remove(world);
        scheduler.unscheduleAllEvents(this);

        world.addEntity(frozenMiner);
    }
}
