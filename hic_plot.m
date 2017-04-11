clear;
load('hic_matrix.mat');

for i = 1:size(hic,1)
    for j = 1:size(hic,2)
        hic(j,i) = hic(i,j);
    end
end

chr_res = 50000;
map_res = 1000;

map = [ones(map_res + 1,1) (1.0:-1.0/map_res:0)' (1.0:-1.0/map_res:0)'];

[xs,ys] = find(hic > 0);

imagesc(hic)
axis equal
axis([xs(1)-1 xs(end) ys(1)-1 ys(end)])
colormap(map)

title('Plot of TADs in given data');
xlabel('Chromosome Position');
ylabel('Chromosome Position');

xticks=[cellstr(num2str(get(gca,'xtick')'*chr_res))];
yticks=[cellstr(num2str(get(gca,'ytick')'*chr_res))];

set(gca, 'xticklabel', xticks);
set(gca, 'yticklabel', yticks);