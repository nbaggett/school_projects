import processing.core.PImage;
import java.util.List;
import java.util.Optional;

public class OreBlob extends AnimatedEntity
{
    private String QUAKE_KEY = "quake";

    public OreBlob(String id, Point position, List<PImage> images, int actionPeriod, int animationPeriod)
    {
        super(id, position, images, actionPeriod, animationPeriod);
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler) {
        Optional<Entity> blobTarget = Movable.findNearest(world, super.getPosition(), Vein.class);
        long nextPeriod = super.getActionPeriod();

        if (blobTarget.isPresent()) {
            Point tgtPos = blobTarget.get().getPosition();

            if (moveTo(scheduler, world, blobTarget.get())) {
                Quake quake = new Quake(super.getId(), tgtPos, imageStore.getImageList(QUAKE_KEY));

                world.addEntity(quake);
                nextPeriod += super.getActionPeriod();
                quake.scheduleActions(scheduler, world, imageStore);
            }
        }

        scheduler.scheduleEvent(this, new Activity(this, world, imageStore), nextPeriod);
    }

}
